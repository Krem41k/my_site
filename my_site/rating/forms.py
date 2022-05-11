from django import forms

from main.models import CustomUser

from .models import Rating
from .utils import RatingMixinForm


class RatingForm(RatingMixinForm):
    user = forms.ModelChoiceField(label='Пользователь', queryset=CustomUser.objects.filter(is_teacher=True),
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Rating
        fields = ('grade', 'comment', 'user',)


class RatingDetailForm(RatingMixinForm):
    class Meta:
        model = Rating
        fields = ('grade', 'comment',)
