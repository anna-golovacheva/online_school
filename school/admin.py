from django.contrib import admin

from school.models import Lesson, Course


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {"slug": ("name", "description")}


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'pk')
    prepopulated_fields = {"pk": ("name", "description")}
