from django.shortcuts import render
import datetime as dt


# Create your views here.
def landingpage(request):
    return render(request,'landingpage.html')

def maps(request):
    return render(request, 'map.html')