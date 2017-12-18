from django import forms
from .models import *


# Default form for this application

class HomeForm(forms.Form):	

	# input field for this form		
	post = forms.CharField()
