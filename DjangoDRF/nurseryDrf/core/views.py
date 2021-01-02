from django.forms import model_to_dict
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Plant, OrderItems, Order
from .serializers import PlantSerializer, OrderItemsSerializer, OrderSerializer

# Create your views here.

@api_view(['GET'])
def getPlants(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPlants(request):
    serializer = PlantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request,pk):
    item = get_object_or_404(Plant,id=pk)
    data ={}
    data["item"] = model_to_dict(item)
    data["quantity"] = request.data["quantity"]
    data["user"] = model_to_dict(request.user)
    order_item = OrderItemsSerializer(data=data)
    if order_item.is_valid():
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(id=pk).exists():
                order_item.quantity +=1
                order_item.save()
        else:
            order = Order.objects.create(user=request.user)
            order.items.add(order_item)
    return Response(order_item.data)

@api_view(['GET'])
def viewOrders(request):
    orders = Order.objects.get()
    serializer = OrderSerializer(orders, many=False)
    return Response(serializer.data)