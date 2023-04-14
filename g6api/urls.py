from django.contrib import admin
from django.urls import path,include

admin.site.site_header = 'G6AI'                    # default: "Django Administration"
admin.site.index_title = 'G6AI Site administration'                 # default: "Site administration"
admin.site.site_title = 'G6AI admin' # default: "Django site admin"

urlpatterns = [
    
    path('', include("chatv1.urls")),
    path('api/v1/auth/', include("accounts.urls")),
    # path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
