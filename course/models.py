from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

# Create your models here.


class Course(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Creator'),
        related_name='creator',
    )
    assistant = models.ManyToManyField(
        User, blank=True,
        verbose_name=_('Assistant'),
        related_name='assistant',
    )
    student = models.ManyToManyField(
        User,
        verbose_name=_('Student'),
        related_name='student',
    )
    english_title = models.CharField(
        max_length=50,
        verbose_name=_('English title'),
    )
    persian_title = models.CharField(
        max_length=50,
        verbose_name=_('Persian title'),
    )
    image = models.ImageField(
        upload_to='course/',
        verbose_name=_('Image'),
    )
    description = models.TextField(
        max_length=1000,
        verbose_name=_('Description'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.english_title


class CourseNotice(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name=_('Course'),
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Creator'),
    )
    description = models.TextField(
        max_length=1000,
        verbose_name=_('Description'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _('Course notice')
        verbose_name_plural = _('Courses notices')

    def __str__(self):
        return str(self.course)


class CourseFile(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name=_('Course'),
    )
    file = models.FileField(
        upload_to='course/file/',
        verbose_name=_('File'),
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )
    icon = models.ImageField(
        upload_to='course/file/icon/',
        blank=True,
        null=True,
        verbose_name=_('Icon'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _('Course file')
        verbose_name_plural = _('Course files')

    def __str__(self):
        return str(self.course)
