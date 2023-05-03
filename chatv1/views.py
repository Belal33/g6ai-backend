from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    ListAPIView
)
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FileUploadParser
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

import openai

from .serializers import ChatBoxSerializer,ChatMessageSerializer
from .models import ChatBox ,ChatMessage
from .Paginations import CustomPagination




class ApiUploadFile(APIView):
    parser_classes = (FileUploadParser,)
    permission_classes=[AllowAny]
    def post(self, request, format="webm"):
        file_obj = request.data.get('file', None)
        if not file_obj:
            return Response(
                {'error': 'Please provide a file'},
                status=status.HTTP_400_BAD_REQUEST
            )
        print(file_obj.name)
        print(file_obj.file)
        # Perform any additional validation on the file here

        try:
            # Estimate the size of the file
            file_size = file_obj.size
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Return the estimated file size
        return Response(
            {'file_size': file_size},
            status=status.HTTP_200_OK
        )

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(allow_empty_file=False,required =True)

    def validated_file(self,value):
        max_size = 5242
        # valid_file_format =[""]
        if value.size > max_size:
            raise serializers.ValidationError("file too large")
        return value


class FileUploadView(CreateAPIView):
    permission_classes=[AllowAny]
    parser_classes=[MultiPartParser]
    serializer_class=FileUploadSerializer
    def post(self,request):
        file_serializer = FileUploadSerializer(data=request.data)
        
        if file_serializer.is_valid() :
            file = file_serializer.validated_data.get("file",None)
            print(dir(file))
            for i in range(5):
                try:
                # Estimate the size of the file
                    res = openai.Audio.transcribe("whisper-1", file)
                    print(res.text)
                    size = file.size
                    duration = size / 128_000 * 8
                    break
                except Exception as e:
                    if i == 4:
                        return Response(
                            {'error': str(e)}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                        )
            
            
            return Response(
                {
                    "content":res.text,
                    "size":size,
                    "duration":round(duration),
                },
                status=status.HTTP_202_ACCEPTED
                )
        
        return Response(
            # {"error":"something wrong"}
            dict(file_serializer.errors),
            
            status=status.HTTP_400_BAD_REQUEST
        )
        


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

class ChatMessageListCreateView(ListAPIView):
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
