from django.urls import path, include
from django.views.generic import TemplateView
from .views import (
    file_upload_view,
    FileUploadView,
    ApiUploadFile,
    ChatBoxListCreateView,
    ChatBoxRetrieveDestroyView,
    ChatMessageListCreateView,
)


############################
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class ChatView(TemplateView):
    template_name = "chatv1/indexws.html"


############################

urlpatterns = [
    # api/v1/chat/
    # api/v1/chat/chatboxes/
    # api/v1/chat/chatboxes/<chatbox_id>/
    # api/v1/chat/messages/<chatbox_id>/
    # api/v1/chat/messages/e359fbf3-62d1-4a4d-bb8a-dfc59a7cf07f/
    path("", ChatView.as_view()),
    path("messages/<chatbox_id>/", ChatMessageListCreateView.as_view()),
    path("chatboxes/<pk>/", ChatBoxRetrieveDestroyView.as_view()),
    path("voice/", FileUploadView.as_view()),
    # path("file/", ApiUploadFile.as_view()),
    path("file/", file_upload_view),
    path("chatboxes/", ChatBoxListCreateView.as_view()),
]
