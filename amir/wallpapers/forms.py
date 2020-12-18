from django import forms
from .models import Wallpapers

class WallpaperForm(forms.ModelForm):
    class Meta:
        model=Wallpapers
        fields=[
            "image",
            "title"
        ]