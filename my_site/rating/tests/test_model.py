from django.test import TestCase

from main.models import CustomUser
from rating.models import Rating


class RatingModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(username='test', password='qwerty', email='test@mail.ru',
                                         is_teacher=True, university='НГТУ', faculty='АВТФ',
                                         group='АА-87')
        Rating.objects.create(grade=5, comment='great', user=user)

    def test_grade_label(self):
        author = Rating.objects.get(id=1)
        field_label = author._meta.get_field('grade').verbose_name
        self.assertEquals(field_label, 'grade')

    def test_comment_label(self):
        author = Rating.objects.get(id=1)
        field_label = author._meta.get_field('comment').verbose_name
        self.assertEquals(field_label, 'comment')

    def test_user_label(self):
        author = Rating.objects.get(id=1)
        field_label = author._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')

    def test_grade_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.grade
        self.assertEquals(field_value, 5)

    def test_comment_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.comment
        self.assertEquals(field_value, 'great')

    def test_rating_username_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.username
        self.assertEquals(field_value, 'test')

    def test_rating_password_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.password
        self.assertEquals(field_value, 'qwerty')

    def test_rating_email_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.email
        self.assertEquals(field_value, 'test@mail.ru')

    def test_rating_is_teacher_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.is_teacher
        self.assertEquals(field_value, True)

    def test_rating_university_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.university
        self.assertEquals(field_value, 'НГТУ')

    def test_rating_faculty_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.faculty
        self.assertEquals(field_value, 'АВТФ')

    def test_rating_group_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.group
        self.assertEquals(field_value, 'АА-87')

    def test_grade_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.grade
        self.assertNotEqual(field_value, 2)

    def test_comment_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.comment
        self.assertNotEqual(field_value, 'gr')

    def test_rating_username_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.username
        self.assertNotEqual(field_value, 'testsdfg')

    def test_rating_password_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.password
        self.assertNotEqual(field_value, 'sadg')

    def test_rating_email_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.email
        self.assertNotEqual(field_value, 'tesasdf@mail.ru')

    def test_rating_is_teacher_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.is_teacher
        self.assertNotEqual(field_value, False)

    def test_rating_university_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.university
        self.assertNotEqual(field_value, 'НГУ')

    def test_rating_faculty_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.faculty
        self.assertNotEqual(field_value, 'РЭФ')

    def test_rating_group_false_value(self):
        rating = Rating.objects.get(id=1)
        field_value = rating.user.group
        self.assertNotEqual(field_value, 'АА-88')