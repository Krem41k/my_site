from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import TextInput, EmailInput, PasswordInput
from django.shortcuts import redirect


class CustomUserForm(UserCreationForm):
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


class ProfileFormMixin(forms.ModelForm):
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


class ProfileMixinPassesTest(UserPassesTestMixin):
    def test_func(self):
        is_yourself = self.request.user.pk == self.kwargs['pk']
        return is_yourself

    def handle_no_permission(self):
        return redirect('login')
