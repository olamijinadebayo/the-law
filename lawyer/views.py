from django.shortcuts import render

# Create your views here.
def lawyerdashboard(request):
    return render(request, 'law/lawyerdashboard.html')

def lawyerprofile(request):
    return render(request,'law/profile.html')

def lawyercases(request):
    return render(request, 'law/viewcase.html')
