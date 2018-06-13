from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth import authenticate, login
=======
from django.contrib.auth.forms import UserCreationForm
>>>>>>> 15b5f196be2a8a1f05285581b6b55f5b0416b216
from .forms import CitizenSignUpForm, LawyerSignUpForm
from citizen.models import Citizen
from lawyer.models import Lawyer
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
# Create your views here.


def home(request):
    return render(request, 'index.html')


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
            login(request, user)
        return redirect('lawyer:signup')
    else:
        form = CitizenSignUpForm()
    return render(request, 'signup.html', {'form': form})


def lawyer_signup(request):
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
            login(request, user)
        return redirect('lawyer:lawyerdashboard')
    else:
        form = LawyerSignUpForm()
    return render(request, 'lawyer_signup.html', {'form': form})
