from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserModifyForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")
