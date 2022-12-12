from django import forms
from .models import ReservationEvent

class ReservationEventForm(forms.ModelForm) :
    class Meta:
        model = ReservationEvent
        fields = [
            'title',
            'description',
            'location',
            'duration_in_minutes',
            'event_type',
            'max_spots',
            'color_hex_code',
            'event_link',
            'internal_note',
            'display_spots_number'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'title',
                'class': 'form-control',
                'placeholder': 'Event title',
                }),
            'description': forms.Textarea(attrs={
                'id': 'description',
                'class': 'form-control',
                'placeholder': 'Description',
                'style': 'height: 100px'
                }),
            'location': forms.Textarea(attrs={
                'id': 'location',
                'class': 'form-control',
                'placeholder': 'Location',
                }),
            'duration_in_minutes': forms.NumberInput(attrs={
                'id': 'duration',
                'class': 'form-control',
                'placeholder': 'Duration (in minutes)',
                'min': '0',
                'max': '1440'
                }),
            'event_type': forms.Select(attrs={
                'id': 'event-type',
                'class': 'form-select'
                }),
            'max_spots': forms.NumberInput(attrs={
                'id': 'max-spots',
                'class': 'form-control',
                'placeholder': 'Max number of spots',
                'min': '0',
                'max': '100',
                }),
            'color_hex_code': forms.TextInput(attrs={
                'type': 'color',
                'id': 'color-hex-code',
                'class': 'form-control',
                'placeholder': 'Color',
                'style': 'cursor: pointer'
                }),
            'event_link': forms.TextInput(attrs={
                'id': 'event-link',
                'class': 'form-control',
                'placeholder': 'Event link',
                }),
            'internal_note': forms.Textarea(attrs={
                'id': 'internal-note',
                'class': 'form-control',
                'placeholder': 'Internal note',
                'style': 'height: 100px'
                }),
            'display_spots_number': forms.CheckboxInput(attrs={
                'id': 'display-spots-number',
                'class': 'form-check-input'
            })
        }