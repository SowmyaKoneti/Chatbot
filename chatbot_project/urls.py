# chatbot_project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chatbot.urls')),  # Remove the 'namespace' parameter
    path('', include('chatbot.urls')),
]
