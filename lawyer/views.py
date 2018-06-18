from lawyer.forms import NewArticleForm, ProfileForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Articles, Lawyer, Law
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
    return render(request, 'law/viewcase.html')


def lawyerarticles(request):
    cases = Post.objects.all()
    return render(request, 'law/lawyerarticle.html', {"cases": cases})


def newarticle(request):
    current_user = request.user.id
    profile = Law.objects.get(id=request.user.id)
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
    current_profile = Law.objects.get(id=profile_id)
    return render(request, 'law/lawyerprofile.html', {"current_profile": current_profile})


@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.law)
        if profile_form.is_valid():
            profile_form.save()
            # messages.success(request, _(
            #     'Your profile was successfully updated!'))
            return redirect('accounts:lawyer')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.law)
    return render(request, 'edit_profile.html', {"profile_form": profile_form})
