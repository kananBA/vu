from django.contrib import admin

from .models import CourseTask, CourseTaskStudent

# Register your models here.

class CourseTaskStudentInline(admin.TabularInline):
    model = CourseTaskStudent
    extra = 1

class CourseTaskAdmin(admin.ModelAdmin):
    inlines = [
        CourseTaskStudentInline,
    ]


admin.site.register(CourseTask, CourseTaskAdmin)
