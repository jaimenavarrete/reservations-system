from django.shortcuts import render
from . import views

# Create your views here.
def view_event(request) :
    return render(request, 'reservations/view_event.html')