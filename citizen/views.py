from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from .forms import PostForm

# Create your views here.
def post(request):
    if request.user.is_citizen == True:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                post.citizen = request.user
                form.save() 
                return redirect('accounts:lawyer')
        else:
            form = PostForm()
        return render(request, 'citizen/post.html', {'form': form})
    else:
        return redirect('accounts:citizenSignup')