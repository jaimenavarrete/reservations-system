from django.shortcuts import render
from .forms import ReservationForm

# Create your views here.
def view_event(request) :
    form = ReservationForm()
    
    return render(request, 'reservations/view_event.html', {
        'form': form
    })