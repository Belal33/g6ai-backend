from django.urls import path,include
from django.views.generic import TemplateView
from .views import chat_view
urlpatterns = [
    
    # path('',TemplateView.as_view(template_name='chatv1/index.html')),
    path('',TemplateView.as_view(template_name='chatv1/indexws.html')),
    path('chat/',chat_view),
]