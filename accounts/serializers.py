from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import PasswordResetSerializer

from .forms import MyAllAuthPasswordResetForm


class MyRegisterSerializer(RegisterSerializer):
    password2 = None
    password = serializers.CharField(write_only=True)
    password1 = password

    def validate(self, data):
        return data


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return MyAllAuthPasswordResetForm
