from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm) :
    start_date = forms.DateField(required=False,
                                widget=forms.DateInput(attrs={
                                    'type': 'date',
                                    'id': 'start-date',
                                    'class': 'form-control',
                                    'placeholder': 'Reservation date'
                                    }))

    class Meta :
        model = Reservation
        fields = [
            'name',
            'email',
            'extra_information',
            'start_time',
            'reservation_event'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'class': 'form-control',
                'placeholder': 'Name'
                }),
            'email': forms.TextInput(attrs={
                'id': 'email',
                'class': 'form-control',
                'placeholder': 'Email'
                }),
            'extra_information': forms.Textarea(attrs={
                'id': 'extra-information',
                'class': 'form-control',
                'placeholder': 'Extra information',
                'style': 'height: 100px'
                }),
            'start_time': forms.Select(attrs={
                'id': 'start-time',
                'class': 'form-select',
                'placeholder': 'Reservation time'
                })
        }