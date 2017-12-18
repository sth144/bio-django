from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm

from .process import computeGC
from .models import *


# Default view for this app

class HomeView(TemplateView):

	# Define template for this view
	template_name = 'ComputeGC/form.html'

	# Handle HTTP GET requests through this view

	def get(self, request):

		# Define the form
		form = HomeForm()

		# Render the page with the form included
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle HTTP POST requests through this view

	def post(self, request):

		# Define the form
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():

			# Store cleaned input data
			posted = form.cleaned_data['post']

			# Process data
			result = computeGC(form.cleaned_data['post'])

			# Clear text field
			form = HomeForm()										

		# Render the page with form and result data
		args = {'form': form, 'posted': posted, 'result': result}
		return render(request, self.template_name, args)
