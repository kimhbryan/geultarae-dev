from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreateForm, UserModifyForm
from .models import User


class Admin(UserAdmin):
    add_form = UserCreateForm
    form = UserModifyForm
    model = User
    list_display = ["email", "username",]


admin.site.register(User, Admin)
