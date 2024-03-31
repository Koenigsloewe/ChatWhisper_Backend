import uuid
from django.db import models
from Account.models import UserAccount


# Create your models here.
class ChatInstruction(models.Model):
    instruction = models.TextField(default="""A dialog, where User interacts with AI. AI is helpful, kind, obedient, 
    honest, and knows its own limits. User: Hello, AI. AI: Hello! How can I assist you today?""")

    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='instruction')

    def __str__(self):
        return self.instruction


class ChatConversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    SENDER_CHOICES = [
        ('user', 'User'),
        ('agent', 'Agent'),
    ]
    conversation = models.ForeignKey(ChatConversation, on_delete=models.CASCADE, related_name='message')
    message = models.TextField()
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
