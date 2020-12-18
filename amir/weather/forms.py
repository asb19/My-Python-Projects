from django import forms 

class checkform(forms.Form):
    check_field=forms.BooleanField()