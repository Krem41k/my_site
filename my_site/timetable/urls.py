from django.urls import path

from . import views

urlpatterns = [
    path('<str:group>/', views.show_timetable, name='timetable'),
]