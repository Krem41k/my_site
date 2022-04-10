from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput, CheckboxInput

from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }))
    password1 = forms.CharField(label='Пароль', widget=PasswordInput({
                'class': 'form-control',
                'placeholder': 'Пароль'
            }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=PasswordInput({
        'class': 'form-control',
        'placeholder': 'Подтверждение пароля'
    }))
    email = forms.EmailField(label='Email', widget=EmailInput({
                'class': 'form-control',
                'placeholder': 'Email'
            }))

    is_teacher = forms.BooleanField(label='Вы учитель?')

    university = forms.CharField(label='Университет', widget=TextInput({
        'class': 'form-control',
        'placeholder': 'Университет'
    }))

    faculty = forms.CharField(label='Факультет', widget=TextInput({
        'class': 'form-control',
        'placeholder': 'Факультет'
    }))

    group = forms.CharField(label='Группа', widget=TextInput({
        'class': 'form-control',
        'placeholder': 'Группа'
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'is_teacher',
                  'university', 'faculty', 'group']
