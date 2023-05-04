from django.urls import path, include, re_path
from django.views.generic import TemplateView
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
    UserDetailsView,
)
from dj_rest_auth.registration.views import SocialAccountListView, ConfirmEmailView

from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework_simplejwt.views import TokenVerifyView

from .views import (
    GoogleLogin,
    MyRegisterView,
)  # , google_callback, oauth2_callback, oauth2_login

# from allauth.account.views import confirm_email as allauthemailconfirmation


urlpatterns = [
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    # for the get response => for test
    # path('password/reset/confirm/<uidb64>/<token>/',
    #   TemplateView.as_view(template_name="password_reset_confirm.html"),
    #   name='password_reset_confirm'),
    # for the get response => for test
    path(
        "password/reset/confirm/<slug:uidb64>/<slug:token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "registration/account-confirm-email/<key>/",
        ConfirmEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path("", include("dj_rest_auth.urls")),
    # URLs that do not require a session or valid token
    # path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    # path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    # path('login/', LoginView.as_view(), name='rest_login'),
    # # URLs that require a user to be logged in with a valid session / token.
    # path('logout/', LogoutView.as_view(), name='rest_logout'),
    # path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    # path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    # path("registration/", MyRegisterView.as_view()),
    path("registration/", include("dj_rest_auth.registration.urls")),
    # path('socialaccounts/', SocialAccountListView.as_view(), name='social_account_list'),
    path("google/", GoogleLogin.as_view(), name="google_login"),
    # path('', include('allauth.socialaccount.providers.google.urls')),
    # "google/login/"
    # "google/login/callback/
]
# api/v1/auth/ password/reset/ [name='rest_password_reset']
# api/v1/auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
# api/v1/auth/ login/ [name='rest_login']
# api/v1/auth/ logout/ [name='rest_logout']
# api/v1/auth/ user/ [name='rest_user_details']
# api/v1/auth/ password/change/ [name='rest_password_change']
# api/v1/auth/ registration/  [name='rest_register']
# api/v1/auth/ registration/verify-email/  [name='rest_verify_email']
# api/v1/auth/ registration/resend-email/  [name='rest_register']
