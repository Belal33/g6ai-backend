from dj_rest_auth.registration.serializers import RegisterSerializer


class MyRegisterSerializer(RegisterSerializer):
  password2 = None

  def validate(self, data):
      return data

# class RegisterSerializer(serializers.Serializer):

    # password1 = serializers.CharField(write_only=True)
    # password2 = None

    # def validate_username(self, username):
    #     username = get_adapter().clean_username(username)
    #     return username

    # def validate_email(self, email):
    #     email = get_adapter().clean_email(email)
    #     if allauth_settings.UNIQUE_EMAIL:
    #         if email and email_address_exists(email):
    #             raise serializers.ValidationError(
    #                 _('A user is already registered with this e-mail address.'),
    #             )
    #     return email

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
