from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser


class CustomUseCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = CustomUser
    fields = UserCreationForm.Meta.fields + ("age",)



class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = CustomUser  
    fields = "__all__"  