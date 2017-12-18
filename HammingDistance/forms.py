from django import forms
from .models import *


# Default form for this app

class HomeForm(forms.Form):

	# text fields for input
	post = forms.CharField()
	against = forms.CharField()
