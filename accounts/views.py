from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CitizenSignUpForm, LawyerSignUpForm
from citizen.models import Citizen
from lawyer.models import Lawyer
from django.contrib.auth import login as dj_login, authenticate, logout as dj_logout
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
# Create your views here.


def citizen(request):
    return render(request, 'citizen.html')


def lawyer(request):
    return render(request, 'lawyer.html')


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
        return redirect('citizen')
    else:
        form = CitizenSignUpForm()
    return render(request, 'signup.html', {'form': form})


def lawyersignup(request):
    if request.method == 'POST':
        form = LawyerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.refresh_from_db()
            user.is_lawyer = True
            user.lawyer.location = form.cleaned_data.get('location')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
        return redirect('lawyer')
    else:
        form = LawyerSignUpForm()
    return render(request, 'lawyer_signup.html', {'form': form})


def login(request):
    if request.GET.get('username') and request.GET.get("password"):
        username = request.GET.get("username")
        password = request.GET.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            if user.is_citizen == True:
                return render(request, 'citizen.html')
            else:
                return render(request, 'lawyer.html')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loginpage(request):
    return render(request, 'login.html')


def logout(request):
    dj_logout(request)
    return redirect('loginpage')
