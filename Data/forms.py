from django import forms
from .models import *


class DNAForm(forms.ModelForm):
    name = forms.CharField()
    sequence = forms.CharField()

    class Meta:
        model = DNASeq
        fields = ('name', 'sequence',)


class RNAForm(forms.ModelForm):
    name = forms.CharField()
    sequence = forms.CharField()

    class Meta:
        model = RNASeq
        fields = ('name', 'sequence',)


class PeptideForm(forms.ModelForm):
    name = forms.CharField()
    sequence = forms.CharField()

    class Meta:
        model = PeptideSeq
        fields = ('name', 'sequence',)
