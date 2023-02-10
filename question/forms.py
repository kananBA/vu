from django import forms

from .models import MultipleChoiceQuestion, DescriptiveQuestion, FileQuestion


class MultipleChoiceQuestionCreateForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestion
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


class DescriptiveQuestionCreateForm(forms.ModelForm):
    class Meta:
        model = DescriptiveQuestion
        fields = (
            'question',
        )

        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
            }),
        }


class FileQuestionCreateForm(forms.ModelForm):
    class Meta:
        model = FileQuestion
        fields = (
            'file',
        )

        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
