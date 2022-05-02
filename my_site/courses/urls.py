from django.urls import path

from . import views
from .views import CourseListView, CourseCreateView, LessonCreateView, SearchResultsView

urlpatterns = [
    path('', CourseListView.as_view(), name='courses'),
    path('new/', CourseCreateView.as_view(), name='create_course'),
    path('new/lesson', LessonCreateView.as_view(), name='create_lesson'),
    path('search/', SearchResultsView.as_view(), name='search_course_results'),
    path('course/<int:pk>', views.course_detail, name='detail_course'),
]
