from django.urls import path
from . import views

urlpatterns = [
    path('view_event/', views.view_event, name='view_event')
]