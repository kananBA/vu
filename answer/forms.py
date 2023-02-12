from django import forms

from .models import MultipleChoiceAnswer, DescriptiveAnswer, FileAnswer


class MultipleChoiceAnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceAnswer
        fields = (
            'answer',
        )

        widgets = {
            'answer': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class DescriptiveAnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = DescriptiveAnswer
        fields = (
            'answer',
        )

        widgets = {
            'question': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class FileAnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = FileAnswer
        fields = (
            'file',
        )

        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control-file',
            }),
        }
