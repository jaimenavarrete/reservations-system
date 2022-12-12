from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime, timedelta
from .forms import ReservationForm
from events.models import ReservationEvent
from .models import Reservation

# Create your views here.
def view_event(request, event_link) :
    searched_event = ReservationEvent.objects.filter(event_link=event_link)
    
    if not searched_event.exists() :
        messages.error(request, "The event does not exist!")
        return redirect('events:index')
    
    event = searched_event[0]
    
    form = ReservationForm(request.POST or None)
    
    if request.method == 'POST' :
        if form.is_valid() :
            form.save()

            messages.success(request, 'The reservation was made successfully')
            return redirect('reservations:view_event', event_link=event_link)
    
    return render(request, 'reservations/view_event.html', {
        'event': event,
        'form': form
    })

def get_reservation_times(request, event_id) :
    searched_event = ReservationEvent.objects.filter(id=event_id)
    
    if not searched_event.exists() :
        response = {
            'result': False,
            'data': None
        }
        return JsonResponse(response)
    
    event = searched_event[0]
    
    # Get the closest duration time that is divisible by 5
    added_time = 0 if event.duration_in_minutes % 5 == 0 else 5 - event.duration_in_minutes % 5
    duration_time = timedelta(minutes=event.duration_in_minutes + added_time)
    
    reservation_times_list = []
    
    first_available_time = datetime.strptime(request.GET.get('date'),'%Y-%m-%d')
    last_available_time = first_available_time + timedelta(days=1) - duration_time
    current_available_time = first_available_time
    
    while current_available_time <= last_available_time :
        time_text = current_available_time.strftime("%Y-%m-%dT%H:%M")
        
        reservation_times_list.append(time_text)
        
        current_available_time += timedelta(minutes=5)

    reservations_list = Reservation.objects.filter(reservation_event_id=event_id)
    
    # Remove times used by other reservations and conflicting times
    for reservation in reservations_list :
        first_conflicting_time = reservation.start_time - duration_time + timedelta(minutes=5)
        last_conflicting_time = reservation.start_time + duration_time - timedelta(minutes=5)
        current_conflicting_time = first_conflicting_time
        
        while current_conflicting_time <= last_conflicting_time :
            time_text = current_conflicting_time.strftime("%Y-%m-%dT%H:%M")
            
            if time_text in reservation_times_list :
                reservation_times_list.remove(time_text)
            
            current_conflicting_time += timedelta(minutes=5)
    
    response = {
        'result': True,
        'data': reservation_times_list
    }

    return JsonResponse(response, safe=False)