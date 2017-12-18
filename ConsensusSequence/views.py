from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm

from .process import *
from .models import *


# Default View for this app

class HomeView(TemplateView):

	# Define HTML template for this app
	template_name = 'ConsensusSequence/form.html'

	# Handle HTTP GET requests through this view

	def get(self, request):

		# Define the form
		form = HomeForm()

		# Render the page with the form
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle Http POST requests through this view

	def post(self, request):
		
		# Define the form
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():

			# Store input data
			posted = form.cleaned_data['post']

			# Process data
			result = consensusSequence(posted)
			form = HomeForm()											

		# Render page with form and result
		args = {'form': form, 'posted': posted, 'result': result}
		return render(request, self.template_name, args)
