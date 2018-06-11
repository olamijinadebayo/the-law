from django import forms 
from .import models 

class NewPostArticle(forms.ModelForm):
    model = Articles 
    exclude = ['time','username']
    