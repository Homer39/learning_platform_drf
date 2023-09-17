from rest_framework import serializers

from payment.services.payment import create_payment
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for payment"""

    class Meta:
        model = Payment
        fields = "__all__"

    def create(self, validated_data):
        payment = Payment(
            payment_amount=validated_data["payment_amount"],
            payment_method=validated_data["payment_method"],
            payment_id=create_payment(validated_data['payment_amount']),
        )
        payment.save()
        return payment
