from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

class wordreaderform(forms.Form):
    word_upload=forms.FileField()