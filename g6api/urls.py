from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "G6AI"  # default: "Django Administration"
admin.site.index_title = "G6AI Site administration"  # default: "Site administration"
admin.site.site_title = "G6AI admin"  # default: "Django site admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/v1/auth/", include("accounts.urls")),
    path("api/v1/chat/", include("chatv1.urls")),
    # http://localhost:8000/accounts/google/login/callback/
]
