from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ChatBoxSerializer,ChatMessageSerializer
from .models import ChatBox ,ChatMessage
from .Paginations import CustomPagination

class ChatBoxListCreateView(ListCreateAPIView):
    serializer_class=ChatBoxSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = ChatBox.objects.filter(user=self.request.user)
        return queryset


class ChatBoxRetrieveDestroyView(RetrieveDestroyAPIView):
    serializer_class=ChatBoxSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = ChatBox.objects.filter(user=self.request.user)
        return queryset

class ChatMessageListCreateView(ListCreateAPIView):
    serializer_class=ChatMessageSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated,]
    
    def perform_create(self, serializer):
        chatbox_id = self.kwargs['chatbox_id']
        chatbox=ChatBox.objects.get(id=chatbox_id)
        # Autofill FK user.
        serializer.save(user=self.request.user,chatbox=chatbox)
    
    def get_queryset(self):
        user = self.request.user
        chatbox_id = self.kwargs['chatbox_id']
        queryset = ChatMessage.objects.filter(user=user, chatbox_id=chatbox_id)
        return queryset
