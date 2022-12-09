from django.db import models

# Create your models here.
class EventType(models.Model) :
    name = models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name
    
class ReservationEvent(models.Model) :
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    internal_note = models.CharField(max_length=200, blank=True)
    duration_in_minutes = models.IntegerField()
    location = models.CharField(max_length=100)
    event_type = models.ForeignKey(EventType, on_delete=models.DO_NOTHING)
    max_spots = models.IntegerField(default=1)
    display_spots_number = models.BooleanField(default=False)
    color_hex_code = models.CharField(max_length=7)
    event_link = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=36)
    modified = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=36, blank=True)
    
    def __str__(self) :
        return self.title