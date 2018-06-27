from lawyer.forms import NewArticleForm, ProfileForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Articles, Lawyer
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db import transaction
from django.contrib import messages
from citizen.models import Citizen, Post, Profile

# Create your views here.


def lawyerdashboard(request):
    return render(request, 'law/lawyerdashboard.html')


def lawyercases(request):
    cases = Post.objects.all()
    return render(request, 'law/viewcase.html',{"cases":cases})


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
