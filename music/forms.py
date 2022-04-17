from django import forms
from django.forms import ModelForm
from .models import Event

#Create a Event Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('club', 'event_name', 'date', 'venue', 'description')
