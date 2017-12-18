from django import forms
from .models import *


# Default form for this app

class HomeForm(forms.Form):

	# text input fields for this form
	post = forms.CharField()
	against = forms.CharField()
