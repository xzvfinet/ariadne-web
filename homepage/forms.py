from django import forms
from .models import Photo


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image_file', 'description',)
        exclude = ('filtered_image_file',)
