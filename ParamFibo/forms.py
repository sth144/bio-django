from django import forms
from .models import *

class HomeForm(forms.Form):
	post = forms.CharField()
	against = forms.CharField()
