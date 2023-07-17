from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    FileUploadView,
    ChatBoxListCreateView,
    ChatBoxRetrieveDestroyView,
    ChatMessageListCreateView,
    AllMessagesListView,
)


############################
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class ChatView(TemplateView):
    template_name = "chatv1/indexws.html"


############################

# api/v1/chat/
# api/v1/chat/chatboxes/
# api/v1/chat/chatboxes/<chatbox_id>/
# api/v1/chat/messages/<chatbox_id>/
# api/v1/chat/messages/e359fbf3-62d1-4a4d-bb8a-dfc59a7cf07f/

urlpatterns = [
    path("", ChatView.as_view()),
    path("messages/<chatbox_id>/", ChatMessageListCreateView.as_view()),
    path("chatboxes/<pk>/", ChatBoxRetrieveDestroyView.as_view()),
    path("chatboxes/", ChatBoxListCreateView.as_view()),
    # for Admin ####
    path("messages/", AllMessagesListView.as_view()),
    path("voice/", FileUploadView.as_view()),
]
