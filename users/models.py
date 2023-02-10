from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    TEACHER = 1
    STUDENT = 2
    ROLE_CHOICES = (
        (TEACHER, _("Teacher")),
        (STUDENT, _("Student")),
    )

    role = models.PositiveSmallIntegerField(
        default=2,
        choices=ROLE_CHOICES,
        verbose_name=_('Role'),
    )
    photo = models.ImageField(
        upload_to='photo/',
        blank=True,
        null=True,
        verbose_name=_('Photo'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username
