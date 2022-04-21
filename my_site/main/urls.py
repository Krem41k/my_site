from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from . import views
from .views import SignUpView, ProfileUpdateView, ProfileLogin

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', ProfileLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
]
