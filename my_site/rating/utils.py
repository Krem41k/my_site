from django import forms
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from main.models import CustomUser


class RatingMixinForm(forms.ModelForm):
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea({
        'class': 'form-control',
        'placeholder': 'Комментарий'
    }), required=False)

    grade = forms.IntegerField(label='Оценка', widget=forms.NumberInput({
        'class': 'form-control',
        'placeholder': 'Оценка'
    }))


class RatingMixinPassesTest(UserPassesTestMixin):
    def test_func(self):
        is_yourself = self.request.user.username != self.kwargs['user']
        return self.request.user.is_teacher is False and is_yourself

    def handle_no_permission(self):
        return redirect('rating')
