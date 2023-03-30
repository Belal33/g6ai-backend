from django.urls import path,include,re_path
from django.views.generic import TemplateView
from dj_rest_auth.registration.views import VerifyEmailView
# from allauth.account.views import confirm_email as allauthemailconfirmation

# from dj_rest_auth.registration.urls 
# from dj_rest_auth.urls

urlpatterns =[
    
    # for the get response => for test
    path('password/reset/confirm/<uidb64>/<token>/',
      TemplateView.as_view(template_name="password_reset_confirm.html"),
      name='password_reset_confirm'),


    
    ####account_confirm_email - You should override this view to handle it in your API client somehow and then,
    ####send post to /verify-email/ endpoint with proper key.
    # ImproperlyConfigured at /api/v1/auth/registration/account-confirm-email/NQ:1phztT:8EioupJYCqG1RtQu9FhYNodDv2KPw2TBQLVehhGVefk/ TemplateResponseMixin requires either a definition of 'template_name' or an implementation of 'get_template_names()'
    # path('registration/account-confirm-email/<token>/', allauthemailconfirmation, name='account_email_verification_sent'),
    path('registration/account-confirm-email/<token>/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
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


