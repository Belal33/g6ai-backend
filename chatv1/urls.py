from django.urls import path
from django.views.generic import TemplateView
from .views import chat_view
urlpatterns = [
    
    path('',TemplateView.as_view(template_name='chatv1/index.html')),
    path('chat/',chat_view),
]
 