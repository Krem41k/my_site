from django.urls import path

from . import views

urlpatterns = [
    path('<str:user_group>/', views.show_timetable, name='timetable'),
]