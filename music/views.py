from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event
from django.core.mail import send_mail
from music.forms import SubscribeForm
from django.conf import settings
from django.contrib import messages
from .forms import EventForm
from django.http import HttpResponseRedirect

def index(request):
	if request.method == "POST":
		form = SubscribeForm(request.POST)
		if form.is_valid():
			subject = "CONTACT SUBMITTED"
			message = "Sending email through Gmail"
			recepient =form.cleaned_data.get('email')
			send_mail(subject, message, settings.EMAIL_HOST_USER, [recepient], fail_silently=False)
			messages.success(request, 'Success!!')
			return render(request, 'index.html', {'form':form})


	event_list = Event.objects.all()
	return render(request, 'index.html', {'event_list' : event_list})

def dashboard(request):
	submitted = False
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard?submitted=True')

	else:
		form = EventForm
		if 'submitted' in request.GET:
			submitted = True
	form = EventForm
	return render(request, 'dashboard.html', {'form':form, 'submitted':submitted})





