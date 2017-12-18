from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm
from .process import reverseComplement

from .models import *


# Default view for this app

class HomeView(TemplateView):

	# Define the template
	template_name = 'ReverseComplement/form.html'

	# Handle HTTP GET requests

	def get(self, request):

		# Define the form
		form = HomeForm()

		# Render the page
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle HTTP POST requests

	def post(self, request):

		# Define the form
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():
			posted = form.cleaned_data['post']
			text = reverseComplement(form.cleaned_data['post'])
			form = HomeForm()											

		# Render the page
		args = {'form': form, 'posted': posted, 'text': text}
		return render(request, self.template_name, args)
