from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm

from .process import *
from .models import *


# Default view for this app

class HomeView(TemplateView):

	# Define the HTML template
	template_name = 'ParseMotif/form.html'

	# Handle HTTP GET requests through this view

	def get(self, request):
		
		# Define the form
		form = HomeForm()

		# Render the page
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle HTTP POST requests through this view

	def post(self, request):

		# Define the form
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():
			posted = form.cleaned_data['post']
			against = form.cleaned_data['against']
			result = parseMotif(posted, against)
			form = HomeForm()				

		# Render page with results							
		args = {
			'form': form, 
			'posted': posted, 
			'against': against,
			'result': result,
		}
		return render(request, self.template_name, args)
