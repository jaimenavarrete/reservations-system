from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime, timedelta
from .forms import ReservationForm

# Create your views here.
def view_event(request) :
    form = ReservationForm()
    
    return render(request, 'reservations/view_event.html', {
        'form': form
    })

def get_reservation_times(request) :
    reservation_times_list = []
    
    duration = 60
    start_time = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    last_time = start_time + timedelta(days=1) - timedelta(minutes=duration)
    
    while start_time <= last_time :
        time = {
            'value': start_time,
            'name': start_time.strftime('%H:%M')
        }
        
        reservation_times_list.append(time)
        
        start_time += timedelta(minutes=5)
    
    return JsonResponse(reservation_times_list, safe=False)