from django.db import models

# Create your models here.

class Club(models.Model):
	name = models.CharField('Club Name', max_length = 120)
	club_head = models.CharField(null = True, max_length = 120)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Event(models.Model):
	club = models.ForeignKey(Club, blank=True, null=True, on_delete=models.CASCADE)
	event_name = models.CharField(max_length = 120)
	date = models.DateTimeField()
	venue = models.CharField('Place', max_length = 120)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.event_name	




