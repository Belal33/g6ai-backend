from django.urls import path,include
from django.views.generic import TemplateView
from .views import (
    ChatBoxListCreateView,
    ChatBoxRetrieveDestroyView,
    ChatMessageListCreateView
)
urlpatterns = [
    # api/v1/chat/
    # api/v1/chat/chatboxes/
    # api/v1/chat/chatboxes/<chatbox_id>/
    # api/v1/chat/messages/<chatbox_id>/
    # api/v1/chat/messages/e359fbf3-62d1-4a4d-bb8a-dfc59a7cf07f/
    path('',TemplateView.as_view(template_name='chatv1/indexws.html')),
    path("messages/<chatbox_id>/",ChatMessageListCreateView.as_view()),
    path("chatboxes/",ChatBoxListCreateView.as_view()),
    path("chatboxes/<pk>/",ChatBoxRetrieveDestroyView.as_view()),
]