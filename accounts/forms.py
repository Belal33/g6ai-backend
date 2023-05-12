from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse

from allauth.account.forms import default_token_generator
from allauth.account.utils import (
    filter_users_by_email,
    user_pk_to_url_str,
    user_username,
)
from allauth.utils import build_absolute_uri
from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from django.contrib.sites.shortcuts import get_current_site
from dj_rest_auth.serializers import AllAuthPasswordResetForm

from .models import CustomUser


# costom reset email url
class MyAllAuthPasswordResetForm(AllAuthPasswordResetForm):
    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data["email"]
        token_generator = kwargs.get("token_generator", default_token_generator)

        for user in self.users:
            temp_key = token_generator.make_token(user)

            path = reverse(
                "password_reset_confirm",
                args=[user_pk_to_url_str(user), temp_key],
            )

            # url = (
            #     f"https://www.chatg6.ai/{str(user_pk_to_url_str(user))}/{str(temp_key)}"
            # )

            url = build_absolute_uri(None, path)
            print(url)

            context = {
                "current_site": current_site,
                "user": user,
                "password_reset_url": url,
                "request": request,
            }
            if (
                app_settings.AUTHENTICATION_METHOD
                != app_settings.AuthenticationMethod.EMAIL
            ):
                context["username"] = user_username(user)
            get_adapter(request).send_mail(
                "account/email/password_reset_key", email, context
            )
        return self.cleaned_data["email"]


# custom user forms
class CustomUseCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = "__all__"
