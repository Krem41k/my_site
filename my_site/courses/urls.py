from django.urls import path

from . import views
from .views import CourseListView, CourseCreateView, LessonCreateView, SearchResultsView, CourseUpdateView, \
    CourseDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='courses'),
    path('new/', CourseCreateView.as_view(), name='create_course'),
    path('search/', SearchResultsView.as_view(), name='search_course_results'),
    path('course/<int:pk>', views.course_detail, name='detail_course'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('course/<int:pk>/new/lesson', LessonCreateView.as_view(), name='create_lesson'),
]
