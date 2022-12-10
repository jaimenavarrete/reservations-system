from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('view_event/<str:event_link>', views.view_event, name='view_event'),
    path('get_reservation_times/', views.get_reservation_times, name='get_reservation_times')
]