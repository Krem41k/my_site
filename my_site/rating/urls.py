from django.urls import path

from . import views
from .views import RatingCreateView

urlpatterns = [
    path('', views.rating_list, name='rating'),
    path('new/', RatingCreateView.as_view(), name='create_rating'),
    path('<str:user>', views.rating_detail, name='detail_rating'),
]
