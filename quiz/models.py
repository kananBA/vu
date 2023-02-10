from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from course.models import Course

# Create your models here.


class Quiz(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name=_('Course'),
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_('Title'),
    )
    duration = models.PositiveIntegerField(
        verbose_name=_('Duration'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')

    def __str__(self):
        return self.title


class QuizStudent(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name=_('Quiz'),
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Student'),
    )
    grade = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_('Grade'),
    )
    is_present = models.BooleanField(
        default=False,
        verbose_name=_('Is present'),
    )

    class Meta:
        verbose_name = _('Quiz student')
        verbose_name_plural = _('Quiz students')

    def __str__(self):
        return str(self.student)
