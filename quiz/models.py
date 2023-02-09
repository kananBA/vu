from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    duration = models.PositiveIntegerField(verbose_name=_('Duration'))
    start_at = models.DateTimeField(verbose_name=_('Start at'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')

    def __str__(self):
        return self.title


class QuizStudent(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('Quiz'))
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Student'))
    grade = models.FloatField(blank=True, null=True, verbose_name=_('Grade'))
    is_present = models.BooleanField(default=False, verbose_name=_('Is present'))

    class Meta:
        verbose_name = _('Quiz student')
        verbose_name_plural = _('Quiz students')

    def __str__(self):
        return self.english_title


class QuizMultipleChoiceQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('Quiz'))
    first_choice = models.CharField(max_length=30, verbose_name=_('First choice'))
    second_choice = models.CharField(max_length=30, verbose_name=_('Second choice'))
    third_choice = models.CharField(max_length=30, verbose_name=_('Third choice'))
    forth_choice = models.CharField(max_length=30, verbose_name=_('Forth choice'))

    class Meta:
        verbose_name = _('Quiz multiple choice question')
        verbose_name_plural = _('Quiz multiple choice questions')

    def __str__(self):
        return str(self.quiz)


class QuizDescriptiveQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('Quiz'))
    question = models.TextField(max_length=1000, verbose_name=_('Answer'))

    class Meta:
        verbose_name = _('Quiz descriptive question')
        verbose_name_plural = _('Quiz descriptive questions')

    def __str__(self):
        return str(self.quiz)


class QuizFileQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('Quiz'))
    file = models.FileField(upload_to='quiz/file/', verbose_name=_('File'))

    class Meta:
        verbose_name = _('Quiz file question')
        verbose_name_plural = _('Quiz file questions')

    def __str__(self):
        return str(self.quiz)


class QuizMultipleChoiceAnswer(models.Model):
    quiz_student = models.ForeignKey(QuizStudent, on_delete=models.CASCADE, verbose_name=_('Quiz student'))
    question = models.ForeignKey(QuizMultipleChoiceQuestion, on_delete=models.CASCADE, verbose_name=_('Question'))
    answer = models.CharField(max_length=30, verbose_name=_('Answer'))
    grade = models.FloatField(verbose_name=_('Grade'))

    class Meta:
        verbose_name = _('Quiz multiple choice student')
        verbose_name_plural = _('Quiz multiple choice students')

    def __str__(self):
        return str(self.quiz_student)


class QuizDescriptiveAnswer(models.Model):
    quiz_student = models.ForeignKey(QuizStudent, on_delete=models.CASCADE, verbose_name=_('Quiz student'))
    question = models.ForeignKey(QuizDescriptiveQuestion, on_delete=models.CASCADE, verbose_name=_('Question'))
    answer = models.TextField(max_length=1000, verbose_name=_('Answer'))
    grade = models.FloatField(verbose_name=_('Grade'))

    class Meta:
        verbose_name = _('Quiz descriptive answer')
        verbose_name_plural = _('Quiz descriptive answers')

    def __str__(self):
        return str(self.quiz_student)


class QuizFileAnswer(models.Model):
    quiz_student = models.ForeignKey(QuizStudent, on_delete=models.CASCADE, verbose_name=_('Quiz student'))
    question = models.ForeignKey(QuizFileQuestion, on_delete=models.CASCADE, verbose_name=_('Question'))
    file = models.FileField(upload_to='quiz/file/', verbose_name=_('File'))
    grade = models.FloatField(verbose_name=_('Grade'))

    class Meta:
        verbose_name = _('Quiz file answer')
        verbose_name_plural = _('Quiz file answers')

    def __str__(self):
        return str(self.quiz_student)
