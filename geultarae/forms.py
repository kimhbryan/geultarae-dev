from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    pass
    # class Meta:
    #     model = User
    #     fields = ("username", "email")


class UserModifyForm(UserChangeForm):
    pass
    # class Meta:
    #     model = User
        # fields = ("username", "email")


class AskForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
