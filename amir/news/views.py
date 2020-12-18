from django.shortcuts import render, redirect
import math
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
from datetime import timedelta, timezone, datetime
import os
import shutil

from .models import Headline, UserProfile

def news_list(request):
    user_p=UserProfile.objects.filter(user=request.user).first()
    now=datetime.now(timezone.utc)
    timediff=now-user_p.last_scraped
    timediff_in_hours=timediff/timedelta(minutes=60)
    new_scrape=24-timediff_in_hours
    if timediff_in_hours <=24:
        hide_me=True
    else:
        hide_me=False

    headlines=Headline.objects.all()
    context={'headlines':headlines,
             'new_scrape':math.ceil(new_scrape),
             'hide_me':hide_me

    }
    return render(request,'news/home.html',context)



def scrape(request):
    user_p=UserProfile.objects.filter(user=request.user).first()
    user_p.last_scraped=datetime.now(timezone.utc)
    user_p.save()

    s=requests.session()
    url='https://www.hindustantimes.com/'
    content=s.get(url,verify=False).content
    soup=BeautifulSoup(content,'html.parser')
    listings=soup.find_all('div',{'class':'media'})

    for item in listings[:4]:
        link,title=item.find_all('a')[1]['href'],item.find_all('a')[1]['title']
        image_src=item.find('img',{'class':'lazy'})['data-src']
        
        media_root='/Users/ASB/projects/amir/media'
        if not image_src.startswith(("data:image", "javascript")):
            local_filename=image_src.split('/')[-1]
            ir=s.get(image_src,stream=True,verify=False)
            with open(local_filename,'wb') as f:
                for chunk in ir.iter_content(chunk_size=1024):
                    f.write(chunk)
        shutil.move(local_filename,media_root)
        new_headline=Headline()
        new_headline.title=title
        new_headline.url=link
        new_headline.image=local_filename
        new_headline.save()
        print(new_headline.title)
        print(user_p.user)
    return redirect('home')
def current(request):
    return redirect('https://www.youtube.com/playlist?list=PLLRM7ROnmA9HEta6gV4j4h2WfmIOC23EH')