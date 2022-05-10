from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput

from .models import CustomUser
from .utils import ProfileFormMixin


class RegisterStudentForm(ProfileFormMixin):
    group = forms.CharField(label='Группа', widget=TextInput({
        'class': 'form-control',
        'placeholder': 'Группа'
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name',
                  'email', 'university', 'faculty', 'group']


class RegisterTeacherForm(ProfileFormMixin):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name',
                  'email', 'university', 'faculty']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UpdateUserForm(ProfileFormMixin):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'university', 'faculty', 'group']
