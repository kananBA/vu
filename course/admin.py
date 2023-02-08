from django.contrib import admin

from .models import Course, CourseNotice, CourseFile

# Register your models here.

class CourseNoticeInline(admin.TabularInline):
    model = CourseNotice
    extra = 1

class CourseFileInline(admin.TabularInline):
    model = CourseFile
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [
        CourseNoticeInline,
        CourseFileInline,
    ]

admin.site.register(Course, CourseAdmin)
