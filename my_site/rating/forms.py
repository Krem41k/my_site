from django import forms

from main.models import CustomUser

from .models import Rating


class RatingForm(forms.ModelForm):
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea({
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }))
    grade = forms.IntegerField(label='Оценка', widget=forms.NumberInput({
                'class': 'form-control',
                'placeholder': 'Оценка'
            }))
    user = forms.ModelChoiceField(label='Пользователь', queryset=CustomUser.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Rating
        fields = ('grade', 'comment', 'user',)


class RatingDetailForm(forms.ModelForm):
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea({
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }))
    grade = forms.IntegerField(label='Оценка', widget=forms.NumberInput({
                'class': 'form-control',
                'placeholder': 'Оценка'
            }))

    class Meta:
        model = Rating
        fields = ('grade', 'comment',)
