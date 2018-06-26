from django import forms
from .models import Articles, Lawyer


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        exclude = ['time', 'lawyer',]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        exclude = ['user',]
