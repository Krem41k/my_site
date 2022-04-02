from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class DocumentCreateView(CreateView):
    template_name = 'library/create_document.html'
    success_url = reverse_lazy('library')
