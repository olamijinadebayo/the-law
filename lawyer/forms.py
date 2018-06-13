from django import forms 
from .models import Articles

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Articles 
        exclude = ['time','username']

class ProfileForm(forms.ModelForm):
    class Meta:
        # model = Profile
        exclude = ['time','first_name','email','last_name']
        
