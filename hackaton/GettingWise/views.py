from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to GettingWise by team that does not have a name yet!")
    return render(request, 'GettingWise/index.html')