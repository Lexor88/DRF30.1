from rest_framework import serializers
from .models import Course, Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'  # Выводим все поля урока

class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()  # Количество уроков
    lessons = LessonSerializer(many=True, read_only=True)  # Список уроков

    class Meta:
        model = Course
        fields = '__all__'  # Включаем все поля + lesson_count + lessons

    def get_lesson_count(self, obj):
        return obj.lessons.count()  # Подсчёт уроков
