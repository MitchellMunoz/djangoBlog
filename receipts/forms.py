# receipts/forms.py
from django import forms

class ReceiptForm(forms.Form):
    image       = forms.ImageField()
    total       = forms.DecimalField(max_digits=9, decimal_places=2, required=False)
    merchant    = forms.CharField(max_length=120, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
