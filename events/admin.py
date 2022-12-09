from django.contrib import admin
from .models import EventType, ReservationEvent

# Register your models here.
admin.site.register(EventType)
admin.site.register(ReservationEvent)