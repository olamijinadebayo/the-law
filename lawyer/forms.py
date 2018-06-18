from django import forms
from .models import Articles, Lawyer, Law


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        exclude = ['time', 'lawyer']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Law
        exclude = ['user']
