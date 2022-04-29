from django import forms
from django.forms import ModelForm
from .models import Event

#Create a Event Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('event_name', 'date', 'venue', 'description')

# Creating a Email Form
class SubscribeForm(forms.Form):
	email = forms.EmailField()


