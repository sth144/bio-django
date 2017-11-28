from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AnonymousUser, User

# Create your models here.

class Blurb(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User, default=1) # FIX
	date = models.DateTimeField(auto_now=True)