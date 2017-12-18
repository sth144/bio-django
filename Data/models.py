from django.db import models

from django.db import models
from django.contrib.auth.models import AnonymousUser, User


# DNA Sequence model class

class DNASeq(models.Model):

	# text data fields
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)


# RNA Sequence model class

class RNASeq(models.Model):

	# text data fields
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)


# Peptide Sequence model class

class PeptideSeq(models.Model):

	# text data fields
    name = models.CharField(max_length=500)
    sequence = models.CharField(max_length=2000)
