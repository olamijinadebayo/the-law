from lawyer.forms import NewPostForm, ProfileForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Articles, Lawyer, Law
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db import transaction
from .forms import ProfileForm
from django.contrib import messages

# Create your views here.


def lawyerdashboard(request):
    return render(request, 'law/lawyerdashboard.html')


def lawyerprofile(request):
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


# def change_lawyerProfile(request, user_id):
#     profile = request.user.profile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             form.save(commit=False)
#             profile.save()
#             return redirect('profile', user_id)
#
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     return render(request, 'lawyer_editprofile.html', {"form": form})

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
