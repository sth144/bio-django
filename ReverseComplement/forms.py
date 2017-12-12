from django import forms
from .models import *

class HomeForm(forms.Form):			# as opposed to forms.Form
	post = forms.CharField()
