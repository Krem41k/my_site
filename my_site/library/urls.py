from django.urls import path

from . import views
from .views import DocumentCreateView, DocumentListView

urlpatterns = [
    path('', DocumentListView.as_view(), name='library'),
    path('new/', DocumentCreateView.as_view(), name='create_document'),
]
