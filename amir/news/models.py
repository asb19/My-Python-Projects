from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save


class Headline(models.Model):
	title = models.TextField(max_length=200)
	image = models.ImageField(null=True,blank=True)
	url = models.URLField(null=True,blank=True)

	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	last_scraped = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}-{}".format(self.user, self.last_scraped)



