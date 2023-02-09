from django.contrib import admin

from .models import Quiz, QuizMultipleChoiceQuestion, QuizDescriptiveQuestion, QuizFileQuestion, QuizStudent, QuizMultipleChoiceAnswer, QuizDescriptiveAnswer, QuizFileAnswer

# Register your models here.

class QuizMultipleChoiceQuestionTabularInline(admin.TabularInline):
    model = QuizMultipleChoiceQuestion
    extra = 0


class QuizDescriptiveQuestionTabularInline(admin.TabularInline):
    model = QuizDescriptiveQuestion
    extra = 0


class QuizFileQuestionTabularInline(admin.TabularInline):
    model = QuizFileQuestion
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    inlines = [
        QuizMultipleChoiceQuestionTabularInline,
        QuizDescriptiveQuestionTabularInline,
        QuizFileQuestionTabularInline,
    ]

admin.site.register(Quiz, QuizAdmin)


class QuizMultipleChoiceAnswerTabularInline(admin.TabularInline):
    model = QuizMultipleChoiceAnswer
    extra = 0
    readonly_fields = (
        'answer',
        'question',
    )


class QuizDescriptiveAnswerTabularInline(admin.TabularInline):
    model = QuizDescriptiveAnswer
    extra = 0
    readonly_fields = (
        'answer',
        'question',
    )


class QuizFileAnswerTabularInline(admin.TabularInline):
    model = QuizFileAnswer
    extra = 0
    readonly_fields = (
        'file',
        'question',
    )


class QuizStudentAdmin(admin.ModelAdmin):
    inlines = [
        QuizMultipleChoiceAnswerTabularInline,
        QuizDescriptiveAnswerTabularInline,
        QuizFileAnswerTabularInline,
    ]

admin.site.register(QuizStudent, QuizStudentAdmin)
