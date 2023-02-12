from django import forms

from .models import CourseTaskStudent


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = CourseTaskStudent
        fields = (
            'file',
        )

        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
