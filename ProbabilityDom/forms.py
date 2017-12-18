from django import forms
from .models import *


# Default form for this app

class HomeForm(forms.Form):

	# text input fields for this form
	k = forms.CharField()
	m = forms.CharField()
	n = forms.CharField()