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
	template_name = 'Translator/form.html'

	def get(self, request):
		form = HomeForm()
		args = {'form': form,}
		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			posted = form.cleaned_data['post']
			result = translate(posted)
			form = HomeForm()											# clear text field
			# return redirect('form/form.html')							# refresh page (?)
		args = {
			'form': form, 
			'posted': posted, 
			'result': result,
		}
		return render(request, self.template_name, args)
