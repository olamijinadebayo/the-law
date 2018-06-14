from django.shortcuts import render
import datetime as dt 

# Create your views here.
def landingpage(request):
    return render(request,'landingpage.html')