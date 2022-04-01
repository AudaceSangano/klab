import email
import imp
from django import forms

class CustomPaymentForm(forms.Form):
    amount = forms.IntegerField()
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
