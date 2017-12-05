from django.db import models

from django.db import models
from django.contrib.auth.models import AnonymousUser, User

# Create your models here.

class DNASeq(models.Model):
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)

class RNASeq(models.Model):
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)

class PeptideSeq(models.Model):
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)
