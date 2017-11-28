from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView
from form.forms import HomeForm
from .process import simpleProcess

from .models import *

# Create your views here.
# def index(request):
    #return HttpResponse('Hello from Python!')
    #return render(request, 'form/form.html')

class HomeView(TemplateView):
	template_name = 'form/form.html'

	def get(self, request):
		form = HomeForm()
		posts = Blurb.objects.all()
		print(posts)
		for item in posts:
			item.post = simpleProcess(item.post)
		args = {'form': form, 'posts': posts}
		return render(request, self.template_name, args)

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			_post = form.save(commit=False)
			_post.user = request.user
			_post.save()
			text = form.cleaned_data['post']
			form = HomeForm()											# clear text field
			# return redirect('form/form.html')							# refresh page (?)
		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)
