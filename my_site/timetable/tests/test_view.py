from django.test import TestCase

from django.urls import reverse


class ViewsTestCase(TestCase):
    def test_url_timetable_exists(self):
        response = self.client.get('/timetable/АА-87/')
        self.assertEqual(response.status_code, 200)

    def test_url_timetable_accessible_by_name(self):
        response = self.client.get(reverse('timetable', kwargs={'user_group': "АА-87"}))
        self.assertEqual(response.status_code, 200)

    def test_timetable_view_uses_correct_template(self):
        response = self.client.get(reverse('timetable', kwargs={'user_group': "АА-87"}))
        self.assertTemplateUsed(response, 'timetable/index.html')
