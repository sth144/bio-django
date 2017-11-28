from django import forms
from .models import *

class HomeForm(forms.ModelForm):			# as opposed to forms.Form
	post = forms.CharField()

	class Meta:
		model = Blurb
		fields = ('post',)					# store as tuple, not string
