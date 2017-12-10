from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def db(request):

    DNASeqs = DNASeq.objects.all()
    RNASeqs = RNASeq.objects.all()
    PeptideSeqs = PeptideSeq.objects.all()

    return render(request, 'db.html', {
        'DNASeqs': DNASeqs,
        'RNASeqs': RNASeqs,
        'PeptideSeqs': PeptideSeqs
    })
