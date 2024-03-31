from django.urls import path
from .views import ChatInstructionAPIView, ChatConversationCreateView, ChatConversationDeleteView, ProcessUserInputView, \
    ChatMessageListView, ChatConversationListView

app_name = "chatbot"

urlpatterns = [
    path('instruction/', ChatInstructionAPIView.as_view(), name='chat_instruction'),
    path('chat/conversation/', ChatConversationCreateView.as_view(), name='create_chat_conversation'),
    path('chat/conversation/<uuid:pk>/', ChatConversationDeleteView.as_view(), name='delete_chat_conversation'),
    path('chat/conversation/<uuid:conversation_id>/process_input/', ProcessUserInputView.as_view(),
         name='process_user_input'),
    path('chat/conversation/<uuid:conversation_id>/messages/', ChatMessageListView.as_view(), name='chat_message_list'),
    path('conversations/', ChatConversationListView.as_view(), name='get_all_conversations')
]
