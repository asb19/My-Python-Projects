from django.shortcuts import render
from .serializers import EmpSerializer
from rest_framework.views import APIView
from .models import Employees
from rest_framework import response
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class employeeView(ModelViewSet):
    # def get(self,request):

    queryset=Employees.objects.all()
    serializer_class=EmpSerializer
    

    