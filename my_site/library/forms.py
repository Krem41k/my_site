from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Название'
            }))
    author = forms.CharField(widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Автор'
            }))
    document = forms.FileField(widget=forms.FileInput({
                'class': 'form-control',
                'placeholder': 'Файл'
            }))

    class Meta:
        model = Document
        fields = ('title', 'author', 'document',)
