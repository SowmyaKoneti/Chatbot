from django.apps import AppConfig
from django.urls import path
from .views import chatbot_view

class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
    app_label = 'chatbot'  # Add this line to set the app_label

urlpatterns = [
    path('chatbot/', chatbot_view, name='chatbot'),
]
