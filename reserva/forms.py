from django import forms

class ReservarForm(forms.Form):
	identificador = forms.CharField(max_length=10)
