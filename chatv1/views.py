from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    ListAPIView,
)
import io
import base64


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from rest_framework.decorators import api_view, parser_classes, permission_classes

import openai


from .serializers import ChatBoxSerializer, ChatMessageSerializer
from .models import ChatBox, ChatMessage
from .Paginations import CustomPagination

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@api_view(["POST"])
@permission_classes([AllowAny])
@parser_classes([FileUploadParser])
@csrf_exempt
def file_upload_view(request, format_file="webm"):
    file = request.data.get("file", None)
    print(dir(file))
    if not file:
        return Response(
            {"error": "Please provide a file"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Check the file format
    valid_formats = [format_file]
    file_ext = file.name.split(".")[-1]
    if file_ext not in valid_formats:
        return Response(
            {
                "error": f"Invalid file file format{file_ext}. Valid formats are {', '.join(valid_formats)}."
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    for i in range(5):
        try:
            size = file.size
            # Estimate the size of the file
            with open(file.name, "rb") as f:
                res = openai.Audio.transcribe("whisper-1", f)
            duration = size / 128_000 * 8
            break
        except Exception as e:
            if i == 4:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

    return Response(
        {
            "content": res.text,
            "size": size,
            "duration": round(duration),
        },
        status=status.HTTP_202_ACCEPTED,
    )


class ApiUploadFile(APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = [AllowAny]

    def post(self, request, format="webm"):
        file = request.data.get("file", None)
        if not file:
            return Response(
                {"error": "Please provide a file"}, status=status.HTTP_400_BAD_REQUEST
            )
        print(file.name)
        print(file.file)
        # Perform any additional validation on the file here

        for i in range(5):
            try:
                # Estimate the size of the file
                print("file: ", file)
                res = openai.Audio.transcribe("whisper-1", file)
                print(res.text)
                size = file.size
                duration = size / 128_000 * 8
                break
            except Exception as e:
                if i == 4:
                    return Response(
                        {"error": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

        return Response(
            {
                "content": res.text,
                "size": size,
                "duration": round(duration),
            },
            status=status.HTTP_202_ACCEPTED,
        )
        # # Return the estimated file size
        # return Response({"file_size": file_size}, status=status.HTTP_200_OK)


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(allow_empty_file=False, required=True)

    def validated_file(self, value):
        max_size = 5242
        # valid_file_format =[""]
        if value.size > max_size:
            raise serializers.ValidationError("file too large")
        return value


@method_decorator(csrf_exempt, name="dispatch")
class FileUploadView(CreateAPIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]
    serializer_class = FileUploadSerializer

    def post(self, request):
        # print(dict(request.data))
        file = request.FILES.get("file", None)
        file_serializer = FileUploadSerializer(data={"file": file})
        print("dict(request.data)" * 50)
        print(file.content_type)
        print("dict(request.data)" * 50)

        if file_serializer.is_valid():
            file = file_serializer.validated_data.get("file", None)
            print(dir(file))
            # ['DEFAULT_CHUNK_SIZE', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_get_name', '_name', '_set_name', 'charset', 'chunks', 'close', 'closed', 'content_type', 'content_type_extra', 'encoding', 'field_name', 'file', 'fileno', 'flush', 'isatty', 'multiple_chunks', 'name', 'newlines', 'open', 'read', 'readable', 'readinto', 'readline', 'readlines', 'seek', 'seekable', 'size', 'tell', 'truncate', 'writable', 'write', 'writelines']
            print(file.name)
            for i in range(5):
                try:
                    res = openai.Audio.transcribe("whisper-1", file)
                    print(res.text)
                    size = file.size
                    duration = size / 128_000 * 8
                    break
                except Exception as e:
                    if i == 4:
                        return Response(
                            {"error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        )
                    # size = file.size
                    # duration = size / 128_000 * 8
                    # f = file.file
                    # f.name = file.name
                    # res = openai.Audio.transcribe("whisper-1", f)

            return Response(
                {
                    "content": res.text,
                    "size": size,
                    "duration": round(duration),
                },
                status=status.HTTP_202_ACCEPTED,
            )
        return Response(
            # {"error":"something wrong"}
            dict(file_serializer.errors),
            status=status.HTTP_400_BAD_REQUEST,
        )


class ChatBoxListCreateView(ListCreateAPIView):
    serializer_class = ChatBoxSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = ChatBox.objects.filter(user=self.request.user)
        return queryset


class ChatBoxRetrieveDestroyView(RetrieveDestroyAPIView):
    serializer_class = ChatBoxSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        queryset = ChatBox.objects.filter(user=self.request.user)
        return queryset


class ChatMessageListCreateView(ListAPIView):
    serializer_class = ChatMessageSerializer
    pagination_class = CustomPagination
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        chatbox_id = self.kwargs["chatbox_id"]
        chatbox = ChatBox.objects.get(id=chatbox_id)
        # Autofill FK user.
        serializer.save(user=self.request.user, chatbox=chatbox)

    def get_queryset(self):
        user = self.request.user
        chatbox_id = self.kwargs["chatbox_id"]
        queryset = ChatMessage.objects.filter(user=user, chatbox_id=chatbox_id)
        return queryset
