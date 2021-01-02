from rest_framework import serializers
from .models import Plant,OrderItems,Order

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plant
        fields='__all__'

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItems
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'