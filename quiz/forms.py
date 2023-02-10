from django import forms
from django.forms.models import inlineformset_factory

from .models import Quiz, QuizMultipleChoiceQuestion, QuizDescriptiveQuestion, QuizFileQuestion


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


class QuizMultipleChoiceCreateForm(forms.ModelForm):
    class Meta:
        model = QuizMultipleChoiceQuestion
        fields = (
            'question',
            'first_choice',
            'second_choice',
            'third_choice',
            'forth_choice',
        )

        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
            }),
            'first_choice': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'second_choice': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'third_choice': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'forth_choice': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }

class QuizDescriptiveQuestionCreateForm(forms.ModelForm):
    class Meta:
        model = QuizDescriptiveQuestion
        fields = (
            'question',
        )

        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
            }),
        }

class QuizFileQuestionCreateForm(forms.ModelForm):
    class Meta:
        model = QuizFileQuestion
        fields = (
            'file',
        )

        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
