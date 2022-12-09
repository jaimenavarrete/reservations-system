from django.db import models
from events.models import ReservationEvent

# Create your models here.
class Reservation(models.Model) :
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    extra_information = models.TextField(blank=True)
    start_time = models.DateTimeField()
    reservation_event = models.ForeignKey(ReservationEvent, on_delete=models.CASCADE)
    
    def __str__(self) :
        return f'{self.name} - {self.reservation_event.title}'