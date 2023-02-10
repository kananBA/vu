from django import forms

from .models import Quiz


class QuizCreateForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = (
            'title',
            'duration',
        )

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }
