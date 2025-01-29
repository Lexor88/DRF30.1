from django.contrib.auth.models import AbstractUser
from django.db import models
from lessons.models import Course, Lesson  # Импортируем модели курсов и уроков

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'  # Логин по email
    REQUIRED_FIELDS = ['username']  # Что ещё запрашивать при регистрации

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Используем CustomUser
    payment_date = models.DateTimeField(auto_now_add=True)
    paid_course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    paid_lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)

    def __str__(self):
        return f'Платеж {self.id} ({self.user.email}) - {self.amount} руб.'
