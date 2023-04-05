from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.urls import reverse 
from django.shortcuts import redirect

import urllib.parse


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/google/login/callback/"
    client_class = OAuth2Client
    
#     def get_callback_url(self, request, *args, **kwargs):
#         return self.request.build_absolute_uri(reverse('custom_google_callback'))


# def google_callback(request, *args, **kwargs):
#     print("=>",dict(request.GET))
#     params = urllib.parse.urlencode(request.GET)
#     print("=>",params)
#     return redirect(f'https://frontend/auth/google',code = params)

# oauth2_login = OAuth2LoginView.adapter_view(GoogleOAuth2Adapter)
# oauth2_callback = OAuth2CallbackView.adapter_view(GoogleOAuth2Adapter)


# url = "code=4%2F0AVHEtk6ADWJYAO8tUvQLwnmW6nSmhj-SEXcNUK7oAkaf8hGOqcVJBkadmNVhtjNaqYU5Sg"
# print(  urllib.parse.unquote(url)
# )

# 8ca3f565b1a1319787a8d17b1a2d0fccc86669d7