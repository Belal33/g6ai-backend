from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from chatv1.admin import ChatBoxInline

from .forms import CustomUseCreationForm,CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUseCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email","password1", "password2"),
            },
        ),
    )
    form = CustomUserChangeForm
    fieldsets = (
        (None, {"fields": ("username", "password",'user_credits')}),
        ("Personal info", {"fields": ("first_name", "last_name", "email","age")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "email",'is_superuser',"is_staff"]
    inlines = [ChatBoxInline]

admin.site.register(CustomUser,CustomUserAdmin)



