from django.apps import AppConfig
from django.conf import settings

from Chatbot.llm_model import LlmModel


class ChatbotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Chatbot"

    def ready(self):
        global llm_model
        llm_model = LlmModel(settings.LLM_MODEL_ABSOLUTE_PATH)
