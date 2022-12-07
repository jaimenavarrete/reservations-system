from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path('', views.index, name='index'),
    path('create_event/', views.create_event, name='create_event'),
    path('edit_event/<int:event_id>', views.edit_event, name='edit_event'),
    path('edit_event_status/', views.edit_event_status, name="edit_event_status"),
    path('delete_event/', views.delete_event, name='delete_event')
]