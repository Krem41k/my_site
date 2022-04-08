from django.test import TestCase

from library.forms import DocumentForm


class TestDocumentForm(TestCase):
    def test_empty_form(self):
        form = DocumentForm()
        self.assertIn('title', form.fields)
        self.assertIn('author', form.fields)
        self.assertIn('document', form.fields)

    def test_DocumentForm_invalid(self):
        form = DocumentForm(data={'title': 'Name', 'author': 'Ivan', 'document': 56})
        self.assertFalse(form.is_valid())
