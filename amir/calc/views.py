from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'amir','age':12})

def getData(request):
    data=request.POST.copy()
    name=data.get('name')
    age=data.get('age')
    return render(request,'enq.html',{'name':name,'age':age})

def add(request):
    val1=request.GET['num1']
    val2=request.GET['num2']
    res=int(val1)+int(val2)
    return render(request,'result.html',{'result':res})