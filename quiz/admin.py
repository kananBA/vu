from django.contrib import admin

from .models import Quiz, QuizStudent
from question.models import MultipleChoiceQuestion, DescriptiveQuestion, FileQuestion
from answer.models import MultipleChoiceAnswer, DescriptiveAnswer, FileAnswer

# Register your models here.

class MultipleChoiceQuestionTabularInline(admin.TabularInline):
    model = MultipleChoiceQuestion
    extra = 0


class DescriptiveQuestionTabularInline(admin.TabularInline):
    model = DescriptiveQuestion
    extra = 0


class FileQuestionTabularInline(admin.TabularInline):
    model = FileQuestion
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    inlines = [
        MultipleChoiceQuestionTabularInline,
        DescriptiveQuestionTabularInline,
        FileQuestionTabularInline,
    ]

admin.site.register(Quiz, QuizAdmin)


class MultipleChoiceAnswerTabularInline(admin.TabularInline):
    model = MultipleChoiceAnswer
    extra = 0
    readonly_fields = (
        'answer',
        'question',
    )


class DescriptiveAnswerTabularInline(admin.TabularInline):
    model = DescriptiveAnswer
    extra = 0
    readonly_fields = (
        'answer',
        'question',
    )


class FileAnswerTabularInline(admin.TabularInline):
    model = FileAnswer
    extra = 0
    readonly_fields = (
        'file',
        'question',
    )


class QuizStudentAdmin(admin.ModelAdmin):
    inlines = [
        MultipleChoiceAnswerTabularInline,
        DescriptiveAnswerTabularInline,
        FileAnswerTabularInline,
    ]

admin.site.register(QuizStudent, QuizStudentAdmin)
