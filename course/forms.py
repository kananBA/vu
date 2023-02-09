from django import forms

from .models import Course

class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            'english_title',
            'persian_title',
            'description',
            'image',
        )

        widgets = {
            'english_title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'persian_title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-controls',
                'rows': 3,
                'cols': 100,
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
            })
        }
