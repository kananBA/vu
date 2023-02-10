from django.db import models
from django.utils.translation import gettext_lazy as _

from quiz.models import QuizStudent
from question.models import MultipleChoiceQuestion, DescriptiveQuestion, FileQuestion

# Create your models here.


class MultipleChoiceAnswer(models.Model):
    quiz_student = models.ForeignKey(
        QuizStudent,
        on_delete=models.CASCADE,
        verbose_name=_('Quiz student'),
    )
    question = models.ForeignKey(
        MultipleChoiceQuestion,
        on_delete=models.CASCADE,
        verbose_name=_('Question'),
    )
    answer = models.CharField(
        max_length=30,
        verbose_name=_('Answer'),
    )
    grade = models.FloatField(
        verbose_name=_('Grade'),
    )

    class Meta:
        verbose_name = _('Quiz multiple choice student')
        verbose_name_plural = _('Quiz multiple choice students')

    def __str__(self):
        return str(self.quiz_student)


class DescriptiveAnswer(models.Model):
    quiz_student = models.ForeignKey(
        QuizStudent,
        on_delete=models.CASCADE,
        verbose_name=_('Quiz student'),
    )
    question = models.ForeignKey(
        DescriptiveQuestion,
        on_delete=models.CASCADE,
        verbose_name=_('Question'),
    )
    answer = models.TextField(
        max_length=1000,
        verbose_name=_('Answer'),
    )
    grade = models.FloatField(
        verbose_name=_('Grade'),
    )

    class Meta:
        verbose_name = _('Quiz descriptive answer')
        verbose_name_plural = _('Quiz descriptive answers')

    def __str__(self):
        return str(self.quiz_student)


class FileAnswer(models.Model):
    quiz_student = models.ForeignKey(
        QuizStudent,
        on_delete=models.CASCADE,
        verbose_name=_('Quiz student'),
    )
    question = models.ForeignKey(
        FileQuestion,
        on_delete=models.CASCADE,
        verbose_name=_('Question'),
    )
    file = models.FileField(
        upload_to='quiz/file/',
        verbose_name=_('File'),
    )
    grade = models.FloatField(
        verbose_name=_('Grade'),
    )

    class Meta:
        verbose_name = _('Quiz file answer')
        verbose_name_plural = _('Quiz file answers')

    def __str__(self):
        return str(self.quiz_student)
