from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeDoneView, PasswordChangeView

from . import views
from .views import SignUpStudentView, ProfileUpdateView, ProfileLogin, SignUpStudentView, SignUpTeacherView

urlpatterns = [
    path('', views.index, name='home'),
    path('choice/', views.choice_registration, name='choice_registration'),
    path('signup_student/', SignUpStudentView.as_view(), name='signup_student'),
    path('signup_teacher/', SignUpTeacherView.as_view(), name='signup_teacher'),
    path('login/', ProfileLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
]
