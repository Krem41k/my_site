from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from .forms import RegisterUserForm, LoginUserForm, UpdateUserForm
from .models import CustomUser


def index(request):
    return render(request, 'main/index.html')


class SignUpView(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


class ProfileLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'


class ProfileUpdateView(UpdateView):
    model = CustomUser
    template_name = 'main/profile_edit.html'
    form_class = UpdateUserForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail', kwargs={'username': self.request.user})


def profile_detail(request, username):
    profile = CustomUser.objects.get(username=username)
    return render(request, 'main/profile_detail.html', {'profile': profile})
