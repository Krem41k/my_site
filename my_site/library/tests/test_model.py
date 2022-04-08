from django.test import TestCase

from library.models import Document


class DocumentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Document.objects.create(title='Name', author='Ivan', document='//A')

    def test_title_label(self):
        doc = Document.objects.get(id=1)
        field_label = doc._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_author_label(self):
        doc = Document.objects.get(id=1)
        field_label = doc._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_document_label(self):
        doc = Document.objects.get(id=1)
        field_label = doc._meta.get_field('document').verbose_name
        self.assertEquals(field_label, 'document')

    def test_title_value(self):
        doc = Document.objects.get(id=1)
        field_value = doc.title
        self.assertEquals(field_value, 'Name')

    def test_author_value(self):
        doc = Document.objects.get(id=1)
        field_value = doc.author
        self.assertEquals(field_value, 'Ivan')

    def test_document_value(self):
        doc = Document.objects.get(id=1)
        field_value = doc.document
        self.assertEquals(field_value, '//A')

    def test_title_false_value(self):
        doc = Document.objects.get(id=1)
        field_value = doc.title
        self.assertNotEqual(field_value, 'askdf')

    def test_author_false_value(self):
        doc = Document.objects.get(id=1)
        field_value = doc.author
        self.assertNotEqual(field_value, 'qweqeq')

    def test_document_false_value(self):
        doc = Document.objects.get(id=1)
        field_value = doc.document
        self.assertNotEqual(field_value, '//a')
