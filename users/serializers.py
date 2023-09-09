from rest_framework import serializers

from payment.srializers import PaymentSerializer
from users.models import User


class UserListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка пользователей"""

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "city", "avatar"]


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для одного пользователя"""
    payments_history = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "city", "avatar", "payments_history"]
