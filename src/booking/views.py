from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from booking.models import pilotEvent

# vue page accueil avec la liste des events
def index(request):
    events = pilotEvent.objects.all()
    return render(request, 'booking/bookingList.html', context= {"events": events})

# vue page de détail d'un event
def event_detail(request, id):
    event = get_object_or_404(pilotEvent, id= id)
    return render(request, 'booking/detail.html', context= {"event": event})