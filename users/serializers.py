from rest_framework import serializers
from .models import CustomUser, Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # Выводим все поля платежа

class UserProfileSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True, read_only=True)  # История платежей

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'phone', 'city', 'avatar', 'payments']
