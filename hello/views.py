from django.shortcuts import render
from django.http import HttpResponse
from Data.models import *

from .models import Greeting


def index(request):
    return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')


def contact(request):
	return render(request, 'contact.html')