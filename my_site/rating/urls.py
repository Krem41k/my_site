from django.urls import path

from . import views
from .views import RatingCreateView, RatingListView, DetailRatingCreateView

urlpatterns = [
    path('', RatingListView.as_view(), name='rating'),
    path('new/', RatingCreateView.as_view(), name='create_rating'),
    path('new/<str:user>', DetailRatingCreateView.as_view(), name='rate_user'),
    path('<str:user>', views.rating_detail, name='detail_rating'),
]
