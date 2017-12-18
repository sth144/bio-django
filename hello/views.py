from django.shortcuts import render
from django.http import HttpResponse
from Data.models import *

from .models import Greeting


# Handle index requests

def index(request):

	# render index
    return render(request, 'index.html')


# Handle about request

def about(request):
	
	# render about
	return render(request, 'about.html')


# Handle contact request

def contact(request):

	# render contact
	return render(request, 'contact.html')