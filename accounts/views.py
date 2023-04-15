from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.urls import reverse 
from django.shortcuts import redirect

import urllib.parse
from .serializers import MyRegisterSerializer

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/google/login/callback/"
    client_class = OAuth2Client


# https://www.rootstrap.com/blog/how-to-integrate-google-login-in-your-django-rest-api-using-the-dj-rest-auth-library