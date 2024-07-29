from django import forms
from mainapp.models import AddtoCart
from django.contrib.auth.models import User



class AddtocartForm(forms.ModelForm):
    class Meta:
        model=AddtoCart
        fields=['quantity']