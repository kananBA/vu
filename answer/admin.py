from django.contrib import admin

from .models import MultipleChoiceAnswer, DescriptiveAnswer, FileAnswer

# Register your models here.

admin.site.register(MultipleChoiceAnswer)

admin.site.register(DescriptiveAnswer)

admin.site.register(FileAnswer)
