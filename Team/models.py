from django.db import models
from django.db.models import Count
from djmoney.models.fields import MoneyField
from datetime import timedelta
from django.db.models.signals import post_save
from django.db.models import signals
from django.dispatch import receiver

# Create your models here.


class TeamMembers(models.Model):
	first_name = models.CharField(max_length=100, verbose_name="First Name")
	last_name = models.CharField(max_length=100, verbose_name="Last Name")
	phone = models.CharField(max_length=100, verbose_name="Phone Number")
	email = models.CharField(max_length=100, verbose_name="Email")
	join = models.DateField(verbose_name="Joining Date")
	pending = models.IntegerField(default=0)
	closed = models.IntegerField(default=0)


	def __str__(self):
		return str(self.first_name + " " + self.last_name)
