from django.test import TestCase

from rating.forms import RatingForm

from main.models import CustomUser
from rating.models import Rating


class TestRatingForm(TestCase):
    def test_empty_form(self):
        form = RatingForm()
        self.assertIn('grade', form.fields)
        self.assertIn('comment', form.fields)
        self.assertIn('user', form.fields)

    def test_RatingForm_valid(self):
        user = CustomUser.objects.create(username='test', password='qwerty', email='test@mail.ru',
                                         is_teacher=True, university='НГТУ', faculty='АВТФ',
                                         group='АА-87')
        form = RatingForm(data={'grade': 5, 'comment': 'great', 'user': user})
        self.assertTrue(form.is_valid())

    def test_RatingForm_invalid(self):
        user = CustomUser.objects.create(username='test', password='qwerty', email='test@mail.ru',
                                         is_teacher=True, university='НГТУ', faculty='АВТФ',
                                         group='АА-87')
        form = RatingForm(data={'grade': 'asdf', 'comment': 'great', 'user': user})
        self.assertFalse(form.is_valid())
