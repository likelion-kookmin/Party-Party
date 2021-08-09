from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib.auth import get_user_model

User = get_user_model()


class signupForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = [
            "id",
            "password1",
            "password2",
            "name",
            "nickname",
            "phone_num",
            "email",
            "twitter",
            "item",
            "profile_img",
        ]
