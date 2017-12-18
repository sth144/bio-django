from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm

# Import process and models
from .process import *
from .models import *


# Default view for this app

class HomeView(TemplateView):

	# template for this view
	template_name = 'BaseDistribution/form.html'

	# Handle HTTP GET requests through this view
	
	def get(self, request):

		# Define the form
		form = HomeForm()

		# Render the page with form included
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle HTTP POST requests through this view

	def post(self, request):

		# Define the form
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():

			# Store data from input field
			posted = form.cleaned_data['post']

			# Calculate results
			result = baseDistribution(posted)
			total = sum(result)
			distribution = []
			for i in range(0, len(result)):
				distribution.append(str((result[i] / total)))

			# clear text field
			form = HomeForm()
		
		# Render the page with new args
		args = {
			'form': form, 
			'posted': posted, 
			'result': result,
			'distribution': distribution
		}
		return render(request, self.template_name, args)
