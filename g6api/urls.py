from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('', include("chatv1.urls")),
    path('api/v1/auth/', include("accounts.urls")),

    path('admin/', admin.site.urls),
]
