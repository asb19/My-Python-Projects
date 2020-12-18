from django import forms

from .models import destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model=destination
        fields=[
            "name",
            "desc",
            
        ]