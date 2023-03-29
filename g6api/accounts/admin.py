from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

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
              "fields": ("username","password1", "password2"),
          },
      ),
  )
  form = CustomUserChangeForm
  fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
  list_display = ["username", "email", "is_staff"]
  

admin.site.register(CustomUser,CustomUserAdmin)



