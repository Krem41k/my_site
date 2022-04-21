from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from .forms import RegisterUserForm
from .models import CustomUser


def index(request):
    return render(request, 'main/index.html')


class SignUpView(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


class ProfileUpdateView(UpdateView):
    model = CustomUser
    template_name = 'main/profile_edit.html'
    fields = ['first_name', 'last_name', 'email', 'university', 'faculty', 'group']
    success_url = reverse_lazy('home')


def profile_detail(request, username):
    user = CustomUser.objects.filter(username=username).first()
    return render(request, 'main/profile_detail.html', {'user': user})
