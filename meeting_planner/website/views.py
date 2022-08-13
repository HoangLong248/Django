from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting, Room

# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html', 
                {"meetings": Meeting.objects.all(),"rooms": Room.objects.all(), "name": "Long Tran"})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

# Please add: An about page that shows some text about yourself
def about(request):
    return HttpResponse("Hello Django Project on Pluralsight. My name is John.") 