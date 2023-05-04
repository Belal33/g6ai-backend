from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView, RegisterView

from rest_framework.response import Response
from rest_framework import status

from chatv1.models import ChatBox


class GoogleLogin(
    SocialLoginView
):  # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/google/login/callback/"
    client_class = OAuth2Client


# https://medium.com/codex/google-sign-in-rest-api-with-python-social-auth-and-django-rest-framework-4d087cd6d47f


class MyRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        ChatBox.objects.create(name="ChatG6")

        return Response(
            self.get_response_data(user),
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
