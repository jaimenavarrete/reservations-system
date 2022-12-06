from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .models import ReservationEvent

# Create your views here.
def index(request) :
    reservation_events = ReservationEvent.objects.all()
    
    return render(request, 'events/index.html', {
        'reservation_events': reservation_events
        })
    
def create_event(request) :
    if(request.method == 'POST') :
        ReservationEvent.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            internal_note = request.POST['internal-note'],
            duration = request.POST['duration'],
            time_unit_id = 1,
            location = request.POST['location'],
            event_type_id = request.POST['event-type'],
            max_spots = request.POST['max-spots'],
            display_current_spots_number = request.POST.get('display-current-spots-number', False),
            color_hex_code = request.POST['color-hex-code'],
            event_link = request.POST['event-link'],
            created_by = 'userid'
        )

        messages.success(request, "The event was created successfully!")
        
        return redirect('events:index')
    
    return render(request, 'events/create_event.html')

def edit_event(request, event_id) :
    searched_event = ReservationEvent.objects.filter(id=event_id)
    
    if not searched_event.exists() :
        messages.error(request, "The event does not exist!")
        return redirect('events:index')
    
    event = searched_event[0]
    
    if(request.method == 'POST') :
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.internal_note = request.POST['internal-note']
        event.duration = request.POST['duration']
        event.location = request.POST['location']
        event.event_type_id = request.POST['event-type']
        event.max_spots = request.POST['max-spots']
        event.display_current_spots_number = request.POST.get('display-current-spots-number', False)
        event.color_hex_code = request.POST['color-hex-code']
        event.event_link = request.POST['event-link']
        
        event.save()
        
        messages.success(request, "The event was edited successfully!")
    
        return redirect('events:index')

    return render(request, 'events/create_event.html', {
        'event': event
        })

def delete_event(request) :
    if(request.method == 'GET') :
        Http404()
    
    searched_event = ReservationEvent.objects.filter(id=request.POST['event-id'])
    
    if not searched_event.exists() :
        messages.error(request, "The event does not exist!")
        return redirect('events:index')
    
    event = searched_event[0]
    
    event.delete()
    
    messages.success(request, "The event was deleted successfully!")
    
    return redirect('events:index')