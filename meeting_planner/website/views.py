from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting



def date(request):
    return HttpResponse("This page served at" + str(datetime.now()))



def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})

def home():
    return render(request, "website/website.html", {'name': 'Bob'})

# Create your views here.
