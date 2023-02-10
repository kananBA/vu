from django.db import models
from django.utils.translation import gettext_lazy as _

from course.models import Course
from users.models import User

# Create your models here.


class CourseTask(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name=_('Course'),
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )
    file = models.FileField(
        upload_to='course/file/',
        verbose_name=_('File'),
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name=_('Description'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _('Course task')
        verbose_name_plural = _('Course tasks')

    def __str__(self):
        return str(self.course)


class CourseTaskStudent(models.Model):
    course_task = models.ForeignKey(
        CourseTask,
        on_delete=models.CASCADE,
        verbose_name=_('Course task'),
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Student'),
    )
    file = models.FileField(
        upload_to='course/file/',
        blank=True,
        null=True,
        verbose_name=_('File'),
    )
    grade = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_('Grade'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _('Course task student')
        verbose_name_plural = _('Course task students')

    def __str__(self):
        return str(self.student)
