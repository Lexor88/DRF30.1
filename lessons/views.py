from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Lesson
from .serializers import LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()  # Все записи модели
    serializer_class = CourseSerializer  # Используем наш сериализатор


class LessonListCreateView(ListCreateAPIView):
    queryset = Lesson.objects.all()  # Список уроков
    serializer_class = LessonSerializer


class LessonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()  # Один урок
    serializer_class = LessonSerializer
