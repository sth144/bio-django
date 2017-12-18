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
	template_name = 'ProbabilityDom/form.html'

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

		# Validate the input
		if form.is_valid():
			k = form.cleaned_data['k']
			m = form.cleaned_data['m']
			n = form.cleaned_data['n']

			# process data
			result = probabilityDom(k, m, n)
			form = HomeForm()											
		
		# Render the page
		args = {
			'form': form, 
			'k': k, 
			'm': m,
			'n': n,
			'result': result,
		}
		return render(request, self.template_name, args)
