from django import forms 
from .models import Articles 

class NewPostForm(forms.ModelForm):
    model = Articles 
    exclude = ['time','username']

