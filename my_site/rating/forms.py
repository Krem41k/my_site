from django import forms

from main.models import CustomUser

from .models import Rating


class RatingForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea({
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }))
    grade = forms.IntegerField(widget=forms.NumberInput({
                'class': 'form-control',
                'placeholder': 'Оценка'
            }))
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all())

    class Meta:
        model = Rating
        fields = ('grade', 'comment', 'user',)
