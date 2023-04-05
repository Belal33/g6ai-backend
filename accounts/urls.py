from django.urls import path,include,re_path
from django.views.generic import TemplateView
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView, UserDetailsView,
)
from dj_rest_auth.registration.views import (RegisterView, VerifyEmailView, ResendEmailVerificationView)


from .views import GoogleLogin#, google_callback, oauth2_callback, oauth2_login
# from allauth.account.views import confirm_email as allauthemailconfirmation

# from dj_rest_auth.registration.urls 
# from dj_rest_auth.urls

urlpatterns =[
    
    # for the get response => for test
    path('password/reset/confirm/<uidb64>/<token>/',
      TemplateView.as_view(template_name="password_reset_confirm.html"),
      name='password_reset_confirm'),



    path('registration/account-confirm-email/<token>/', VerifyEmailView.as_view(), name='account_email_verification_sent'),


    #### path('', include('dj_rest_auth.urls')),
    # URLs that do not require a session or valid token
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('login/', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),

    
    #### path('registration/', include('dj_rest_auth.registration.urls')),
    
    path('registration/', RegisterView.as_view(), name='rest_register'),
    path('registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('registration/resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),




    # path('account/', include('allauth.urls')),
]

# from allauth.account.urls
# api/v1/auth/ password/reset/ [name='rest_password_reset']
# api/v1/auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
# api/v1/auth/ login/ [name='rest_login']
# api/v1/auth/ logout/ [name='rest_logout']
# api/v1/auth/ user/ [name='rest_user_details']
# api/v1/auth/ password/change/ [name='rest_password_change']
# api/v1/auth/ registration/  [name='rest_register']
# api/v1/auth/ registration/verify-email/  [name='rest_verify_email']
# api/v1/auth/ registration/resend-email/  [name='rest_register']

# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://localhost:8000&prompt=consent&response_type=code&client_id=770808367137-rbkbstnsbecm98kj53kg0vgr7ocmenlk.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline

# http://localhost:8000/?code=4%2F0AVHEtk6ADWJYAO8tUvQLwnmW6nSmhj-SEXcNUK7oAkaf8hGOqcVJBkadmNVhtjNaqYU5Sg&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile&authuser=0&prompt=consent
