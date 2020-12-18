from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskModel
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def apiovw(request):
    return Response("API OVERVIEW")

@api_view(['GET'])
def tasksview(request):
    tasks=TaskModel.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def taskdetail(request,pk):
    task=TaskModel.objects.get(id=pk)
    serializer=TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request,pk):
    task=TaskModel.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def taskdelete(request,pk):
    task=TaskModel.objects.get(id=pk)
    
    task.delete()
    
    return Response("item deleted")
    