from django import forms
from .models import Articles, Lawyer, Law


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Articles
        exclude = ['time', 'username']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Law
        exclude = ['user']
