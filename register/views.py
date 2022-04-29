from django.shortcuts import render
from django.http import HttpResponse
from music.forms import EventForm

# Create your views here.

def dashboard(request):
	form = EventForm
	return render(request, 'dashboard.html', {})
