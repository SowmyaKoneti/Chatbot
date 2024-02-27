# chatbot/urls.py

from django.urls import path
from .views import chatbot_view, process_input_view

app_name = 'chatbot'  # Add this line to set the app_name

urlpatterns = [
    path('chatbot/', chatbot_view, name='chatbot'),
    path('process_input/', process_input_view, name='process_input'), 
    path('', chatbot_view, name='home'),
]
