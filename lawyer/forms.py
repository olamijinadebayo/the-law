from django import forms 
from .import models 

class NewPostForm(forms.ModelForm):
    model = Articles 
    exclude = ['time','username']

