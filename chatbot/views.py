from django.shortcuts import render
# chatbot/views.py
from django.http import JsonResponse
from .logic.chatbot import handle_input_with_fallback

def chatbot_view(request):
    return render(request, 'chatbot/index.html')

def process_input_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = handle_input_with_fallback(user_input)
        return render(request, 'chatbot/index.html', {'response': response, 'user_input': user_input})
    else:
        return JsonResponse({'error': 'Invalid request method'})