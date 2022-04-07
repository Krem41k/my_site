from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import DocumentForm
from .models import Document


class DocumentListView(ListView):
    model = Document
    template_name = 'library/index.html'
    context_object_name = 'documents'


class DocumentCreateView(CreateView):
    form_class = DocumentForm
    template_name = 'library/create_document.html'
    success_url = reverse_lazy('library')
