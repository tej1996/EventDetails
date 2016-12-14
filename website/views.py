from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'website/index.html')


def dashboard(request):
    return render(request, 'website/dashboard.html')


def profile(request):
    return render(request, 'website/profile.html')



