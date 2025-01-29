"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lessons.views import CourseViewSet
from lessons.views import LessonListCreateView, LessonDetailView
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Добро пожаловать в Django!</h1>")


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', home),  # Главная страница (без отдельного приложения)
    path('admin/', admin.site.urls),  # Админка Django
    path('api/', include(router.urls)),  # API маршруты
    path('api/lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('api/lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('api/', include('users.urls')),  # Подключаем маршруты users
]