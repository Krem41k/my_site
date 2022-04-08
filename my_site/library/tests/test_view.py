from django.test import TestCase

from django.urls import reverse


class ViewsTestCase(TestCase):
    def test_url_library_exists(self):
        response = self.client.get('/library/')
        self.assertEqual(response.status_code, 200)

    def test_url_rating_accessible_by_name(self):
        response = self.client.get(reverse('library'))
        self.assertEqual(response.status_code, 200)

    def test_library_view_uses_correct_template(self):
        response = self.client.get(reverse('library'))
        self.assertTemplateUsed(response, 'library/index.html')

    def test_url_create_document_exists(self):
        response = self.client.get('/library/new/')
        self.assertEqual(response.status_code, 200)

    def test_url_create_document_accessible_by_name(self):
        response = self.client.get(reverse('create_document'))
        self.assertEqual(response.status_code, 200)

    def test_create_document_view_uses_correct_template(self):
        response = self.client.get(reverse('create_document'))
        self.assertTemplateUsed(response, 'library/create_document.html')
