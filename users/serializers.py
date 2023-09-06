from rest_framework import serializers

from payment.srializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя"""
    payments_history = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
