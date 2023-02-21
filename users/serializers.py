from rest_framework import serializers

from school.models import Payment
from users.models import User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'user',
            'date',
            'course',
            'lesson',
            'amount',
            'method_of_payment'
        )


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = (
            'email',
            'avatar',
            'phone',
            'city',
            'payments'
        )
