from django.shortcuts import render

# Create your views here.
def lawyerdashboard(request):
    return render(request, 'law/lawyerdashboard.html')

def lawyerprofile(request):
    return render(request,'law/lawyerprofile.html')

def lawyercases(request):
    return render(request, 'law/viewcase.html')

def lawyerarticles(request):
    return render(request,'law/lawyerarticle.html')