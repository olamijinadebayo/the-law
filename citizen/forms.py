from django import forms
from .models import Post, Citizen


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['citizen']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Citizen
        exclude = ['user']
