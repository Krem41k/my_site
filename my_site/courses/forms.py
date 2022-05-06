from django import forms

from .models import Course, Lesson


class CourseForm(forms.ModelForm):
    title = forms.CharField(label='Название дисциплины', widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Название дисциплины'
            }))
    description = forms.CharField(label='Описание дисциплины', widget=forms.Textarea({
        'class': 'form-control',
        'placeholder': 'Краткое описание'
    }))

    class Meta:
        model = Course
        fields = ['title', 'description']


class LessonForm(forms.ModelForm):
    number = forms.IntegerField(label='Номер урока', widget=forms.NumberInput({
        'class': 'form-control',
        'placeholder': 'Номер урока'
    }))
    name = forms.CharField(label='Название урока', widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'Название урока'
            }))
    content = forms.CharField(label='Содержание урока', widget=forms.Textarea({
        'class': 'form-control',
        'placeholder': 'Содержание урока'
    }))
    material = forms.FileField(label='Файл', widget=forms.FileInput({
        'class': 'form-control',
        'placeholder': 'Файл'
    }))

    class Meta:
        model = Lesson
        fields = ['number', 'name', 'content', 'material']
