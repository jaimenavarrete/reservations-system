from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_event/', views.create_event)
]
