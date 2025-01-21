from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)  # Название курса
    preview = models.ImageField(upload_to='course_previews/', blank=True, null=True)  # Превью
    description = models.TextField(blank=True, null=True)  # Описание

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')  # Связь с курсом
    title = models.CharField(max_length=200)  # Название урока
    description = models.TextField(blank=True, null=True)  # Описание урока
    preview = models.ImageField(upload_to='lesson_previews/', blank=True, null=True)  # Превью
    video_url = models.URLField(blank=True, null=True)  # Ссылка на видео

    def __str__(self):
        return self.title
