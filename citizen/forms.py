from django import forms
from .models import Post, Profile
from django.forms.extras.widgets import SelectDateWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['citizen']


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={"class":"btn btn-primary"}))
    birth_date = forms.DateTimeField(widget=SelectDateWidget)
    class Meta:
        model = Profile
        exclude = ['user']
