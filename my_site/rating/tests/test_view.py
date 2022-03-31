from django.test import TestCase

from django.urls import reverse


class ViewsTestCase(TestCase):
    def test_url_rating_exists(self):
        response = self.client.get('/rating/')
        self.assertEqual(response.status_code, 200)

    def test_url_rating_accessible_by_name(self):
        response = self.client.get(reverse('rating'))
        self.assertEqual(response.status_code, 200)

    def test_rating_view_uses_correct_template(self):
        response = self.client.get(reverse('rating'))
        self.assertTemplateUsed(response, 'rating/index.html')

    def test_url_create_rating_exists(self):
        response = self.client.get('/rating/new')
        self.assertEqual(response.status_code, 200)

    def test_url_create_rating_accessible_by_name(self):
        response = self.client.get(reverse('create_rating'))
        self.assertEqual(response.status_code, 200)

    def test_create_rating_view_uses_correct_template(self):
        response = self.client.get(reverse('create_rating'))
        self.assertTemplateUsed(response, 'rating/create_rating.html')

    def test_url_detail_rating_exists(self):
        response = self.client.get('/rating/testman')
        self.assertEqual(response.status_code, 200)

    def test_url_detail_rating_accessible_by_name(self):
        response = self.client.get(reverse('detail_rating', kwargs={'user': "username"}))
        self.assertEqual(response.status_code, 200)

    def test_detail_rating_view_uses_correct_template(self):
        response = self.client.get(reverse('detail_rating', kwargs={'user': "username"}))
        self.assertTemplateUsed(response, 'rating/details_view.html')
