from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import *
from .models import *


# Not used in current deployment

def db(request):

    DNASeqs = DNASeq.objects.all()
    RNASeqs = RNASeq.objects.all()
    PeptideSeqs = PeptideSeq.objects.all()

    return render(request, 'db.html', {
        'DNASeqs': DNASeqs,
        'RNASeqs': RNASeqs,
        'PeptideSeqs': PeptideSeqs
    })


# DNA Upload view

class DNAView(TemplateView):

    # set template
    template_name = 'data/dnaupload.html'

    # handle HTTP GET requests
    def get(self, request):

        # Define the form
        form = DNAForm()

        # Render the page
        posts = DNASeq.objects.all()
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    # Handle HTTP POST requests for this view
    def post(self, request):

        # Define the form
        form = DNAForm(request.POST)

        # Validate input
        if form.is_valid():
            _post = form.save(commit=False)
            _post.save()
            text = form.cleaned_data['name']
            form = DNAForm()

        # Render the page
        posts = DNASeq.objects.all()
        args = {'form': form, 'text': text, 'posts': posts}
        return render(request, self.template_name, args)


# RNA upload view

class RNAView(TemplateView):

    # Define the template
    template_name = 'data/rnaupload.html'

    # Handle HTTP GET requests

    def get(self, request):

        # Define the form
        form = RNAForm()
        posts = RNASeq.objects.all()

        # Render the page
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    # Handle HTTP POST requests

    def post(self, request):

        # Define the forms
        form = RNAForm(request.POST)

        # Validate the input
        if form.is_valid():
            _post = form.save(commit=False)
            _post.save()
            text = form.cleaned_data['name']
            form = RNAForm()
        posts = RNASeq.objects.all()

        # Render the page
        args = {'form': form, 'text': text, 'posts': posts}
        return render(request, self.template_name, args)


# Peptide Upload view

class PeptideView(TemplateView):

    # Define the template
    template_name = 'data/peptideupload.html'

    # Handle HTTP GET requests for this view

    def get(self, request):

        # Define the form
        form = PeptideForm()
        posts = PeptideSeq.objects.all()
        
        # Render the page
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    # Handle HTTP POST requests for this view

    def post(self, request):

        # Define the form
        form = PeptideForm(request.POST)

        # Validate input
        if form.is_valid():
            _post = form.save(commit=False)
            _post.save()
            text = form.cleaned_data['name']
            form = PeptideForm()
        posts = PeptideSeq.objects.all()

        # Render the page
        args = {'form': form, 'text': text, 'posts': posts}
        return render(request, self.template_name, args)
