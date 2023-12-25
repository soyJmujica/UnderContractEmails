from django.forms import ModelForm
from django import forms
from .models import TeamMembers


class TeamForm(ModelForm):
	"""docstring for TeamForm"""
	class Meta:
		model = TeamMembers
		fields = ['first_name','last_name','phone','email','join']
