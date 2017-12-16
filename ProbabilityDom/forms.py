from django import forms
from .models import *

class HomeForm(forms.Form):
	k = forms.CharField()
	m = forms.CharField()
	n = forms.CharField()