from __future__ import unicode_literals
from django.contrib.auth.models import AnonymousUser, User
from django.db import models

#from django.contrib.auth.models import User

# Create your models here.

class Blurb(models.Model):
	post = models.CharField(max_length=500)
	user = AnonymousUser()
	date = models.DateTimeField(auto_now=True)