from django.contrib import admin
from .models import TimeUnit, EventType, ReservationEvent

# Register your models here.
admin.site.register(TimeUnit)
admin.site.register(EventType)
admin.site.register(ReservationEvent)