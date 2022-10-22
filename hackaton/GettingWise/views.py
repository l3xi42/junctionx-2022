from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage':"Welcome to GettingWise by team that does not have a name yet!"}
    return render(request, 'GettingWise/index.html', context=context_dict)
