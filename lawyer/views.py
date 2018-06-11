from django.shortcuts import render

# Create your views here.
def lawyer(request):
    return render(request, 'law/lawyerdashboard.html')

    