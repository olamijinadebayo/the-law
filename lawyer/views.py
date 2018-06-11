from django.shortcuts import render,redirect
from lawyer.forms import NewPostForm, ProfileForm
import datetime as dt 
from .models import Articles

# Create your views here.
def lawyerdashboard(request):
    return render(request, 'law/lawyerdashboard.html')

def lawyerprofile(request):
    return render(request,'law/lawyerprofile.html')

def lawyercases(request):
    return render(request, 'law/viewcase.html')

def lawyerarticles(request):
    return render(request,'law/lawyerarticle.html')

def newarticle(request):
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_name = current_user
            post.profile = profile

            post.save()
            return redirect('lawyerdashboard')

        else:
            form = NewPostForm()

    return render(request,'new_post.html',{'form':form})

def change_lawyerProfile(request,user_id):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save(commit=False)
            profile.save()
            return redirect('profile', user_id)

    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request,'lawyer_editprofile.html',{"form":form})