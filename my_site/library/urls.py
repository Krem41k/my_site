from django.urls import path

from .views import DocumentCreateView, DocumentListView, SearchResultsView

urlpatterns = [
    path('', DocumentListView.as_view(), name='library'),
    path('new/', DocumentCreateView.as_view(), name='create_document'),
    path('search/', SearchResultsView.as_view(), name='search_document_results'),
]
