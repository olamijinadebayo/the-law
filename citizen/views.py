from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db import transaction
from .forms import PostForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lawyer.models import Lawyer
from .models import Post

# Create your views here.
@login_required
def home(request):
    if request.user.is_citizen == True:
        user_id = request.user.id
        posts = Post.objects.filter(citizen_id=user_id)
        return render(request, 'citizen/home.html',{'posts': posts})
    else:
        return redirect('accounts:citizenSignup')

@login_required
def advocates(request):
    if request.user.is_citizen == True:
        advocates = Lawyer.objects.all()
        return render(request, 'citizen/advocates.html', {'advocates':advocates})
    else:
        return redirect('accounts:citizenSignup')



@login_required()
def post(request):
    if request.user.is_citizen == True:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                post.citizen = request.user
                form.save() 
                return redirect('citizen:edit')
        else:
            form = PostForm()
            # print(request.user.profile.first_name)
            # print(request.user.id)
            # print(Lawyer.objects.all())
        return render(request, 'citizen/post.html', {'form': form})
    else:
        return redirect('accounts:citizenSignup')


@login_required()
@transaction.atomic
def profile_edit(request):
    if request.user.is_citizen == True:
        if request.method == 'POST':
            profile_form = ProfileForm(
                request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                # messages.success(request, _(
                #     'Your profile was successfully updated!'))
                return redirect('citizen:post')
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'citizen/edit-profile.html', {"profile_form": profile_form})
    else:
        return redirect('accounts:citizenSignup')
