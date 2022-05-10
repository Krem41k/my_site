from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect


class TeacherPassesTestMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = 'login/'
    redirect_field_name = 'login'

    def test_func(self):
        return self.request.user.is_teacher

    def handle_no_permission(self):
        return redirect('courses')
