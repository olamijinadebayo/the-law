from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect
from .forms import PostForm

# Create your views here.
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lawyer:signup')
    else:
        form = PostForm()
    return render(request, 'citizen/post.html', {'form': form})