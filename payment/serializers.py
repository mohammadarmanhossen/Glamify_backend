
from rest_framework import serializers
from .models import Checkout, Orderitem


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields ="__all__"

class OrderitemSerializer(serializers.ModelSerializer):
    checkout = CheckoutSerializer(read_only=True) 
    class Meta:
        model = Orderitem
        fields ="__all__"


