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
    user_p=user_p.objects.filter(user=request.user).first()
    user_p.last_scraped=datetime.now(timezone.utc)
    