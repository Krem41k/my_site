from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import RegisterUserForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = RegisterUserForm
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
