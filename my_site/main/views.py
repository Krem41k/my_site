from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from .forms import LoginUserForm, RegisterStudentForm, RegisterTeacherForm, UpdateStudentForm, UpdateTeacherForm
from .models import CustomUser
from .utils import ProfileMixinPassesTest


def index(request):
    return render(request, 'main/index.html')


def choice_registration(request):
    return render(request, 'main/choice_registration.html')


class SignUpStudentView(CreateView):
    form_class = RegisterStudentForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'

    def form_valid(self, form):
        form.instance.is_teacher = False
        return super(SignUpStudentView, self).form_valid(form)


class SignUpTeacherView(CreateView):
    form_class = RegisterTeacherForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'

    def form_valid(self, form):
        form.instance.is_teacher = True
        return super(SignUpTeacherView, self).form_valid(form)


class ProfileLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'


class ProfileUpdateView(ProfileMixinPassesTest, UpdateView):
    model = CustomUser
    template_name = 'main/profile_edit.html'

    def get_form_class(self):
        if self.request.user.is_teacher is False:
            form_class_name = UpdateStudentForm
            return form_class_name
        else:
            form_class_name = UpdateTeacherForm
            return form_class_name

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail', kwargs={'username': self.request.user})


def profile_detail(request, username):
    profile = CustomUser.objects.get(username=username)
    return render(request, 'main/profile_detail.html', {'profile': profile})
