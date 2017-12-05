from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(DNASeq)
admin.site.register(RNASeq)
admin.site.register(PeptideSeq)
