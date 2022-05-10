from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from . import views
from .views import SignUpStudentView, ProfileUpdateView, ProfileLogin, SignUpStudentView, SignUpTeacherView

urlpatterns = [
    path('', views.index, name='home'),
    path('choice/', views.choice_registration, name='choice_registration'),
    path('signup_student/', SignUpStudentView.as_view(), name='signup_student'),
    path('signup_teacher/', SignUpTeacherView.as_view(), name='signup_teacher'),
    path('login/', ProfileLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
]
