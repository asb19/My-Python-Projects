from django.shortcuts import render
import requests

from .models import cityModel
import time

# Create your views here.

def indexView(request):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=792d92241d3cb60c9c82a29297078d8d"
    cities=cityModel.objects.all()

    weather_list=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={
            'city':r['name'],
            'temp':r['main']['temp'],
            'desc':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
            # 'humidity':r['main']['humidity'],
            # 'pressure':r['main']['pressure'],
            # 'wind_deg':r['wind']['deg'],
            # 'wind_spd':r['wind']['speed']
            }
        weather_list.append(city_weather)
    context={'weather_data':weather_list}

    return render(request,'weather/index.html',context)