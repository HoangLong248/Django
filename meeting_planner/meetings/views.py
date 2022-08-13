from django.shortcuts import render
from django.http import Http404

from .models import Meeting, Room

# Create your views here.
def detail(request, id):
    try:
        meeting = Meeting.objects.get(pk=id)
        return render(request, 'meetings/detail.html', {"meeting": meeting})
    except Meeting.DoesNotExist:
        raise Http404("Page not found")

def room_list(request):
    try:
        room = Room.objects.all()
        return render(request, 'meetings/list_room.html', {"rooms": room})
    except Room.DoesNotExist:
        raise Http404("Page not found")