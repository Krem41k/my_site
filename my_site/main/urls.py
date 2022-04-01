from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
