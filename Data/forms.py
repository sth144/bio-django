from django import forms
from .models import *


# Form for DNA sequence upload

class DNAForm(forms.ModelForm):

    # Text fields for name and sequence input
    name = forms.CharField()
    sequence = forms.CharField()

    # Set metadata for this form so that it can update models
    class Meta:
        model = DNASeq
        fields = ('name', 'sequence',)


# Form for RNA sequence upload

class RNAForm(forms.ModelForm):

    # Text fields for name and sequence input
    name = forms.CharField()
    sequence = forms.CharField()

    # Set metadata for this form so that it can update models
    class Meta:
        model = RNASeq
        fields = ('name', 'sequence',)


# Form for peptide sequence upload

class PeptideForm(forms.ModelForm):

    # Text fields for name and sequence input
    name = forms.CharField()
    sequence = forms.CharField()

    # Set metadata for this form so that it can update models
    class Meta:
        model = PeptideSeq
        fields = ('name', 'sequence',)
