from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AnonymousUser, User


# RCSequence model class

class RCSequence(models.Model):

	# Text data fields
	post = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now=True)
