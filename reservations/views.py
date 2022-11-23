from django.shortcuts import render
from .models import ReservationEvent

# Create your views here.
def index(request) :
    reservation_events = ReservationEvent.objects.all()
    
    return render(request, 'reservations/index.html', {
        'reservation_events': reservation_events
    })
    
def create_event(request) :    
    return render(request, 'reservations/create_event.html')