from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('first_name',)


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields =['image_path']