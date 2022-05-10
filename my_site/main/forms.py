from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput

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

    first_name = forms.CharField(label='Имя', widget=TextInput({
        'class': 'form-control',
        'placeholder': 'Имя'
    }))

    last_name = forms.CharField(label='Фамилия', widget=TextInput({
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))

    email = forms.EmailField(label='Email', widget=EmailInput({
                'class': 'form-control',
                'placeholder': 'Email'
            }))

    is_teacher = forms.BooleanField(label='Вы учитель?', required=False)

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
    }), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name',
                  'email', 'is_teacher', 'university', 'faculty', 'group']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=TextInput({
        'class': 'form-control',
        'placeholder': 'Имя'
    }))

    last_name = forms.CharField(label='Фамилия', widget=TextInput({
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))

    email = forms.EmailField(label='Email', widget=EmailInput({
        'class': 'form-control',
        'placeholder': 'Email'
    }))

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
    }), required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'university', 'faculty', 'group']
