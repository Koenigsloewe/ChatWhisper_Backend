from rest_framework import serializers
from .models import ChatInstruction, ChatConversation, ChatMessage


class ChatInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatInstruction
        fields = ['instruction']


class ChatConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatConversation
        fields = ['id', 'name']


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['message', 'sender']
