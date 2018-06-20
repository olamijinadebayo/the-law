from django.shortcuts import render, redirect
from lawyer.forms import NewPostForm, ProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.serializers import serialize
from .forms import LawyerForm,DataForm
from django.contrib.gis.geos import Point
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
import datetime as dt
from .models import Articles, Lawyer, AllLawyer

# Create your views here.


def lawyerdashboard(request):
    return render(request, 'law/lawyerdashboard.html')


def lawyerprofile(request, lawyer_id):
    return render(request, 'law/lawyerprofile.html')


def lawyercases(request):
    return render(request, 'law/viewcase.html')


def lawyerarticles(request):
    return render(request, 'law/lawyerarticle.html')


def newarticle(request):
    # current_user = request.user
    # profile = request.user.profile

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            # post.user_name = current_user
            # post.profile = profile

            post.save()
            return redirect('lawyerdashboard')

    else:
        form = NewPostForm()

    return render(request, 'law/new_post.html', {"form": form})


def change_lawyerProfile(request, user_id):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save(commit=False)
            profile.save()
            return redirect('profile', user_id)

    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'lawyer_editprofile.html', {"form": form})

def portal(request):
    return render(request, 'portal.html')

def lawyer_form(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            new_lawyer = LawyerForm()
            cd = form.cleaned_data
            # print(cd)
            new_lawyer.first_name = cd['first_name']
            new_lawyer.last_name = cd['last_name']
            new_lawyer.phone = cd['phone']
            coordinates = cd['coordinates'].split(',')
            new_lawyer.location = Point(float(coordinates[0]), float(coordinates[1]))
            # print(new_lawyer)
            # new_lawyer.save()

            return redirect('index')
    else:
        form = DataForm()
    return render(request, 'lawyer/lawyer-form.html', {'form': form})

def reported(request):
    lawyers = serialize('geojson', Lawyer.objects.all())
    return HttpResponse(lawyers, content_type='json')

def google(request):
    lawyers = serialize('geojson', AllLawyer.objects.all())
    return HttpResponse(lawyers, content_type='json')


def sms(request):
 
    username = ""
    apikey   = ""
    to = ""
    message = "Risper is not nusty"
    gateway = AfricasTalkingGateway(username, apikey)
    try:
        results = gateway.sendMessage(to, message)
        for recipient in results:
            print('number=%s;status=%s;statusCode=%s;messageId=%s;cost=%s' % (recipient['number'],recipient['status'],recipient['statusCode'],recipient['messageId'],recipient['cost']))
        
    except Exception as e:
        print('Encountered an error while sending: %s' % str(e))
    return None