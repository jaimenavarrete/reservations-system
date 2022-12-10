from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime, timedelta
from .forms import ReservationForm
from events.models import ReservationEvent

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
    response = {
        'result': False,
        'data': None
    }
    
    searched_event = ReservationEvent.objects.filter(id=event_id)
    
    if not searched_event.exists() :
        return JsonResponse(response)
    
    event = searched_event[0]
    reservation_times_list = []
    
    start_time = datetime.strptime(request.GET.get('date'),'%Y-%m-%d')
    last_time = start_time + timedelta(days=1) - timedelta(minutes=event.duration_in_minutes)
    
    while start_time <= last_time :
        time = {
            'value': start_time,
            'name': start_time.strftime('%H:%M')
        }
        
        reservation_times_list.append(time)
        
        start_time += timedelta(minutes=5)
    
    response['result'] = True
    response['data'] = reservation_times_list
    
    return JsonResponse(response, safe=False)