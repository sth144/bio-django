from django.contrib import admin

from .models import *


# Register biomolecular sequence models 

admin.site.register(DNASeq)
admin.site.register(RNASeq)
admin.site.register(PeptideSeq)
