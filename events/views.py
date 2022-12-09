from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ReservationEvent
from .forms import ReservationEventForm

# Create your views here.
def index(request) :
    reservation_events = ReservationEvent.objects.all()
    
    return render(request, 'events/index.html', {
        'reservation_events': reservation_events
        })
    
def create_event(request) :
    form = ReservationEventForm(request.POST or None)
    
    if request.method == 'POST' :        
        if form.is_valid():
            form.save()
            
            messages.success(request, "The event was created successfully!")
            return redirect('events:index')
        
    return render(request, 'events/create_event.html', {
        'form': form
    })

def edit_event(request, event_id) :
    searched_event = ReservationEvent.objects.filter(id=event_id)
    
    if not searched_event.exists() :
        messages.error(request, "The event does not exist!")
        return redirect('events:index')
    
    event = searched_event[0]
    
    form = ReservationEventForm(request.POST or None, instance=event)
    
    if request.method == 'POST' :
        if form.is_valid():
            form.save()
            
            messages.success(request, "The event was edited successfully!")
            return redirect('events:index')

    return render(request, 'events/create_event.html', {
        'event': event,
        'form': form
        })
    
def edit_event_status(request) :
    if request.method != 'POST' :
        messages.error(request, "Invalid operation!")
        return redirect('events:index')

    searched_event = ReservationEvent.objects.filter(id=request.POST['event-id'])
    
    if not searched_event.exists() :
        messages.error(request, "The event does not exist!")
        return redirect('events:index')
    
    event = searched_event[0]
    
    event.active = not event.active
    event.save()
    
    messages.success(request, "The event was edited successfully!")
    
    return redirect('events:index')

def delete_event(request) :
    if request.method != 'POST' :
        messages.error(request, "Invalid operation!")
        return redirect('events:index')
    
    searched_event = ReservationEvent.objects.filter(id=request.POST['event-id'])
    
    if not searched_event.exists() :
        messages.error(request, "The event does not exist!")
        return redirect('events:index')
    
    event = searched_event[0]
    
    event.delete()
    
    messages.success(request, "The event was deleted successfully!")
    
    return redirect('events:index')