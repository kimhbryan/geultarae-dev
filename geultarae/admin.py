from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreateForm, UserModifyForm
from .models import User, Writing


class Admin(UserAdmin):
    add_form = UserCreateForm
    form = UserModifyForm
    model = User
    list_display = ["username", "email", "writings"]
    fieldsets = (
        (None, {
            "fields": (
                ["username", "email", "writings"]
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, Admin)


@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    list_display = ('title', 'hint', 'date_available', 'is_available')
