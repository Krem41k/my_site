from django.urls import path

from . import views
from .views import TeacherListView, RatingCreateView

urlpatterns = [
    path('', TeacherListView.as_view(), name='rating'),
    path('new/', RatingCreateView.as_view(), name='create_rating'),
    path('<str:user>', views.rating_detail, name='detail_rating'),
]
