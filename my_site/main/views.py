from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterUserForm


def index(request):
    return render(request, 'main/index.html')


class SignUpView(generic.CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'



