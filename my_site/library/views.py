from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import DocumentForm
from .models import Document


class DocumentListView(ListView):
    model = Document
    template_name = 'library/index.html'
    context_object_name = 'documents'

    def get_ordering(self):
        ordering = self.request.GET.get('orderby', 'title')
        return ordering


class DocumentCreateView(CreateView):
    form_class = DocumentForm
    template_name = 'library/create_document.html'
    success_url = reverse_lazy('library')


class SearchResultsView(ListView):
    model = Document
    template_name = 'library/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Document.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query)
        )
        return object_list
