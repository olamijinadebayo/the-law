from django import forms 
from .models import Articles, Lawyer

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Articles 
        exclude = ['time','username']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        exclude = ['time','first_name','email','last_name']
        
