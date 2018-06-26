from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CitizenSignUpForm, LawyerSignUpForm
from citizen.models import Citizen
from lawyer.models import Lawyer
from django.contrib.auth import login as dj_login, authenticate, logout as dj_logout
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def citizen(request):
    return render(request, 'citizen.html')

@login_required(login_url='/accounts/login/')
def lawyer(request):
    # current_profile = Law.objects.get(id=profile_id)
    return render(request, 'lawyer.html')
    # return render(request, 'law/lawyerprofile.html', {"current_profile": current_profile})


def citizensignup(request):
    if request.method == 'POST':
        form = CitizenSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_citizen = True
            user.save()
            citizen = Citizen.objects.create(user=user)
            citizen.refresh_from_db()
            citizen.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
        return render(request, 'login.html')
        # return redirect(citizen)
    else:
        form = CitizenSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def lawyer_signup(request):
    if request.method == 'POST':
        form = LawyerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_lawyer = True
            user.save()
            user.refresh_from_db()
            user.lawyer_profile.first_name = form.cleaned_data.get('first_name')
            # lawyer = Lawyer.objects.create(user=user)
            # lawyer.refresh_from_db()
            # lawyer.location = form.cleaned_data.get('location')
            # lawyer.save()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
        # return render(request, 'login.html')
            return redirect('lawyer:lawyerprofile',user.lawyer_profile.id)
    else:
        form = LawyerSignUpForm()
    return render(request, 'lawyer_signup.html', {'form': form})


def login(request):
    if request.POST.get('username') and request.POST.get("password"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            if user.is_citizen == True:
                return redirect('citizen:edit')
            else:
                return redirect('lawyer:lawyerprofile', user.lawyer_profile.id)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loginpage(request):
    return render(request, 'login.html')


def logout(request):
    dj_logout(request)
    return redirect('accounts:loginpage')
