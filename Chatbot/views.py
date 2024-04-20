from django.http import Http404
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatMessageSerializer, ChatConversationSerializer, ChatInstructionSerializer
from .models import ChatInstruction, ChatMessage, ChatConversation
from .apps import llm_model


# Create your views here.

class ChatInstructionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        instruction_instance = ChatInstruction.objects.filter(user=request.user).first()

        if instruction_instance:
            serializer = ChatInstructionSerializer(instruction_instance, data=request.data)
        else:
            serializer = ChatInstructionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        instruction_instance = ChatInstruction.objects.filter(user=request.user).first()

        if instruction_instance:
            serializer = ChatInstructionSerializer(instruction_instance)

            return Response({"instruction": serializer.data.get('instruction')}, status=status.HTTP_200_OK)
        else:
            return Response({"Instruction not found"}, status=status.HTTP_404_NOT_FOUND)


class ChatConversationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChatConversationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatConversationDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ChatConversation.objects.get(pk=pk)
        except ChatConversation.DoesNotExist:
            raise Http404

    def delete(self, request, pk, *args, **kwargs):
        conversation = self.get_object(pk)

        if conversation.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        conversation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProcessUserInputView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, conversation_id, *args, **kwargs):
        try:
            conversation = ChatConversation.objects.get(id=conversation_id, user=request.user)
        except ChatConversation.DoesNotExist:
            return Response({'error': 'Conversation not found.'}, status=404)

        user_input = request.data.get('user_input')
        if not user_input:
            return Response({'error': 'User input is required.'}, status=400)

        ChatMessage.objects.create(
            conversation=conversation,
            message=user_input,
            sender='user'
        )
        instruction_instance = ChatInstruction.objects.filter(user=request.user).first()

        serializer = ChatInstructionSerializer(instruction_instance)

        llm_response = llm_model.get_response(serializer.data.get('instruction'), user_input)

        chat_message = ChatMessage.objects.create(
            conversation=conversation,
            message=llm_response,
            sender='agent'
        )

        serializer = ChatMessageSerializer(chat_message)

        return Response(serializer.data, status=200)


class ChatMessageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, conversation_id, *args, **kwargs):
        conversation = get_object_or_404(ChatConversation, id=conversation_id, user=request.user)

        messages = ChatMessage.objects.filter(conversation=conversation)

        serializer = ChatMessageSerializer(messages, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChatConversationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        conversations = ChatConversation.objects.filter(user=request.user)

        serializer = ChatConversationSerializer(conversations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
