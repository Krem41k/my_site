from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterUserForm
from .models import CustomUser


def index(request):
    return render(request, 'main/index.html')


class SignUpView(generic.CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'


def profile_detail(request, username):
    user = CustomUser.objects.filter(username=username).first()
    return render(request, 'main/profile_detail.html', {'user': user})
