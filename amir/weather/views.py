from django.shortcuts import render,HttpResponse
import requests

from .models import cityModel,TempValue
import time
from .forms import checkform
# Create your views here.

def indexView(request):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=792d92241d3cb60c9c82a29297078d8d"
    cities=cityModel.objects.all()
    weather_list=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        checked=TempValue.objects.get(id=1).incelcius
        if checked:
            temp=int(r['main']['temp'])
            temp=int((temp-32)/1.8)
            print(temp)
            temp=str(temp)+"°C"
        else:
            temp=r['main']['temp']
            temp=str(temp)+"°F"
        city_weather={
            'city':r['name'],
            'temp':temp,
            'desc':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            'humidity':r['main']['humidity'],
           
            # 'pressure':r['main']['pressure'],
            # 'wind_deg':r['wind']['deg'],
            # 'wind_spd':r['wind']['speed']
            }
        weather_list.append(city_weather)
    context={'weather_data':weather_list,'checked':checked}

    return render(request,'weather/index.html',context)


def check(request):
    tempv=request.POST.get('checktemp')
    # print(tempv) checking for the input checkbox value
    obj=TempValue.objects.get(id=1)
    if tempv=='on':
        obj.incelcius=True
    else:
        obj.incelcius=False
    # print(obj.incelcius)  
    obj.save()
    return HttpResponse("")




