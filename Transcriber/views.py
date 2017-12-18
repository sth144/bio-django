from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm

from .process import *
from .models import *


# Default view for this app

class HomeView(TemplateView):

	# Define the template
	template_name = 'Transcriber/form.html'

	# Handle HTTP GET requests through this view

	def get(self, request):

		# Define the view
		form = HomeForm()

		# Render the page
		args = {'form': form,}
		return render(request, self.template_name, args)


	# Handle HTTP POST requests through this view

	def post(self, request):

		# Define the view
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():
			posted = form.cleaned_data['post']
			result = transcribe(posted)
			form = HomeForm()											

		# Render the page
		args = {
			'form': form, 
			'posted': posted, 
			'result': result,
		}
		return render(request, self.template_name, args)
