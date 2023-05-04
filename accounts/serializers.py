from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from chatv1.models import ChatBox


class MyRegisterSerializer(RegisterSerializer):
    password2 = None
    password = serializers.CharField(write_only=True)
    password1 = password

    def create(self, validated_data):
        user = super().create(validated_data)
        ChatBox.objects.create(
            user=user,
            name="ChatG6",
        )
        return user

    def validate(self, data):
        return data


# class RegisterSerializer(serializers.Serializer):

# password2 = None


# def validate_password1(self, password):
#     return get_adapter().clean_password(password)

# def validate(self, data):
#     if data['password1'] != data['password2']:
#         raise serializers.ValidationError(_("The two password fields didn't match."))
#     return data

# def custom_signup(self, request, user):
#     pass

# def get_cleaned_data(self):
#     return {
#         'username': self.validated_data.get('username', ''),
#         'password1': self.validated_data.get('password1', ''),
#         'email': self.validated_data.get('email', ''),
#     }

# def save(self, request):
#     adapter = get_adapter()
#     user = adapter.new_user(request)
#     self.cleaned_data = self.get_cleaned_data()
#     user = adapter.save_user(request, user, self, commit=False)
#     try:
#         adapter.clean_password(self.cleaned_data['password1'], user=user)
#     except DjangoValidationError as exc:
#         raise serializers.ValidationError(
#             detail=serializers.as_serializer_error(exc)
#         )
#     user.save()
#     self.custom_signup(request, user)
#     setup_user_email(request, user, [])
#     return user
