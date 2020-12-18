from django.shortcuts import render, redirect
import math
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
from datetime import timedelta, timezone, datetime
import os
import shutil

from .models import Headline, UserProfile


def scrape(request):
    user_p=UserProfile.objects.filter(user=request.user).first()
    user_p.last_scraped=datetime.now(timezone.utc)
    user_p.save()

    s=requests.session()
    url='https://www.hindustantimes.com/'
    content=s.get(url,verify=False).content
    soup=BeautifulSoup(content,'html.parser')
    listings=soup.find_all('div',{'class':'media'})

    for item in listings[:2]:
        link,title=item.find_all('a')[1]['href'],item.find_all('a')[1]['title']
        image_src=item.find('img',{'class':'lazy'})
        if not image_src.startswith(('data:image','javascript')):
            local_filename=image_src.split('/')[-1]
            ir=s.get(image_src,stream=True,verify=False)
            with open(local_filename,'wb') as f:
                for chunk in ir.iter_content(chunk_size=1024):
                    f.write(chunk)
        new_headline=Headline()
        new_headline.title=title
        new_headline.url=link
        new_headline.image=local_filename
        new_headline.save()
        print(new_headline.title)
    return redirect('list')
def current(request):
    pass
