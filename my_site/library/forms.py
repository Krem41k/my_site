from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    title = forms.CharField(label='Название', widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Название'
            }))
    author = forms.CharField(label='Автор', widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Автор'
            }))
    document = forms.FileField(label='Документ', widget=forms.FileInput({
                'class': 'form-control',
                'placeholder': 'Файл'
            }))

    class Meta:
        model = Document
        fields = ('title', 'author', 'document',)
