from django import forms 
from .models import Articles, Lawyer
from django.forms import ModelForm
from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import PointField

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Articles 
        exclude = ['time','username']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        exclude = ['time','first_name','email','last_name']

class LawyerForm(forms.ModelForm):
    location = PointField()

    class Meta:
        model = Lawyer
        fields = '__all__'

class DataForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50, required=True)
    coordinates=forms.CharField(max_length=200, required=True)
