from lawyer.forms import NewArticleForm, ProfileForm, LawyerForm, DataForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Articles, Lawyer, AllLawyer
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db import transaction
from django.contrib import messages
from citizen.models import Citizen, Post, Profile
from django.http import Http404,HttpResponse
from django.core.serializers import serialize
from .forms import LawyerForm,DataForm
from django.contrib.gis.geos import Point
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)

# Create your views here.


def lawyerdashboard(request):
    return render(request, 'law/lawyerdashboard.html')


def lawyercases(request):
    cases = Post.objects.all()
    drunk = Post.objects.filter(case_category ='Dd')
    land = Post.objects.filter(case_category ='Lf')
    robbery = Post.objects.filter(case_category ='Rb')
    murder = Post.objects.filter(case_category ='Md')
    fraud = Post.objects.filter(case_category ='Fr')
    sex = Post.objects.filter(case_category ='Sa')

    return render(request, 'law/viewcase.html',{"cases":cases,"drunk":drunk,"land":land,"robbery":robbery,"murder":murder,"fraud":fraud,"sex":sex})


def lawyerarticles(request):
    articles = Articles.objects.all()
    return render(request, 'law/lawyerarticle.html', {"articles":articles})


def newarticle(request):
    current_user = request.user.lawyer_profile.id
    profile = Lawyer.objects.get(id=current_user)
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.lawyer = profile
            article.save()
            # redirect not working return redirect('lawyer:profile)
    else:
        form = NewArticleForm()
    return render(request, 'law/new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    current_profile = Lawyer.objects.get(id=profile_id)
    articles = Articles.objects.filter(lawyer=current_profile)
    return render(request, 'law/lawyerprofile.html', {"current_profile": current_profile,"articles":articles})


@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.lawyer_profile)
        if profile_form.is_valid():
            profile_form.save()
            # messages.success(request, _(
            #     'Your profile was successfully updated!'))
            return redirect('lawyer:lawyerprofile',request.user.lawyer_profile.id)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.lawyer_profile)
    return render(request, 'edit_profile.html', {"profile_form": profile_form})

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
    profile_form = ProfileForm(instance=request.user.law)
    return render(request, 'edit_profile.html', {"profile_form": profile_form})
