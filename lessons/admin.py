from django.contrib import admin
from .models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')  # Отображаемые поля
    search_fields = ('title',)  # Поиск по названию курса

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'description')
    search_fields = ('title', 'course__title')  # Поиск по названию урока и курса
    list_filter = ('course',)  # Фильтрация по курсу
