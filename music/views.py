from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event
from django.core.mail import send_mail
from music.forms import SubscribeForm
from django.conf import settings
from django.contrib import messages


# Create your views here.

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

