from django.db import models
from django.utils.translation import gettext_lazy as _

from quiz.models import Quiz

# Create your models here.


class MultipleChoiceQuestion(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name=_('Quiz'),
    )
    question = models.TextField(
        max_length=1000,
        verbose_name=_('Question'),
    )
    first_choice = models.CharField(
        max_length=30,
        verbose_name=_('First choice'),
    )
    second_choice = models.CharField(
        max_length=30,
        verbose_name=_('Second choice'),
    )
    third_choice = models.CharField(
        max_length=30,
        verbose_name=_('Third choice'),
    )
    forth_choice = models.CharField(
        max_length=30,
        verbose_name=_('Forth choice'),
    )

    class Meta:
        verbose_name = _('Quiz multiple choice question')
        verbose_name_plural = _('Quiz multiple choice questions')

    def __str__(self):
        return str(self.quiz)


class DescriptiveQuestion(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name=_('Quiz'),
    )
    question = models.TextField(
        max_length=1000,
        verbose_name=_('Question'),
    )

    class Meta:
        verbose_name = _('Quiz descriptive question')
        verbose_name_plural = _('Quiz descriptive questions')

    def __str__(self):
        return str(self.quiz)


class FileQuestion(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name=_('Quiz'),
    )
    file = models.FileField(
        upload_to='quiz/file/',
        verbose_name=_('File'),
    )

    class Meta:
        verbose_name = _('Quiz file question')
        verbose_name_plural = _('Quiz file questions')

    def __str__(self):
        return str(self.quiz)
