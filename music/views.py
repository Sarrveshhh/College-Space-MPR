from django.http import HttpResponse
from django.shortcuts import render
from .models import Event

# Create your views here.

def index(request):
	event_list = Event.objects.all()
	return render(request, 'index.html', {'event_list' : event_list})


