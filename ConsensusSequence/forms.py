from django import forms
from .models import *


# Default view for this app

class HomeForm(forms.Form):

	# Text field for post input
	post = forms.CharField()
