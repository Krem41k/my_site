from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput

from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(widget=PasswordInput({
                'class': 'form-control',
                'placeholder': 'Пароль'
            }))
    password2 = forms.CharField(widget=PasswordInput({
        'class': 'form-control',
        'placeholder': 'Подтверждение пароля'
    }))
    email = forms.EmailField(widget=EmailInput({
                'class': 'form-control',
                'placeholder': 'Email'
            }))

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'is_teacher', 'university', 'faculty', 'group']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
        }