from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm

from .process import *
from .models import *

# Create your views here.
# def index(request):
    #return HttpResponse('Hello from Python!')
    #return render(request, 'form/form.html')

class HomeView(TemplateView):
	template_name = 'ProbabilityDom/form.html'

	def get(self, request):
		form = HomeForm()
		args = {'form': form,}
		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			k = form.cleaned_data['k']
			m = form.cleaned_data['m']
			n = form.cleaned_data['n']

			# process data
			result = probabilityDom(k, m, n)
			form = HomeForm()											# clear text field
		args = {
			'form': form, 
			'k': k, 
			'm': m,
			'n': n,
			'result': result,
		}
		return render(request, self.template_name, args)
