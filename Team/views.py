from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.utils import timezone
from .models import TeamMembers
from .forms import TeamForm
from Correos.models import UnderContractBuyer
from reportlab.pdfgen import canvas
from django.views.generic import ListView
from django.db.models import Count
# Create your views here.

def AddAgent(request):
	if request.method == 'POST':
		form = TeamForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('agentes')
	else:
		form = TeamForm()
	return render(request, 'addagent.html', {'encabezado':'Add New Agent To The Team',
		'form':form})


def Agents(request):
	agents = TeamMembers.objects.all()
	closed = UnderContractBuyer.objects.values('agent','status').annotate(Count('agent'))
	a = closed.values_list('agent','status','agent__count')
	for agent in agents:
		for count in a:
			if agent.id == count[0]:
				if count[1]=='Pending':
					agent.pending = count[2]
				elif count[1]=='Closed':
					agent.closed = count[2]
		agent.save()


	return render(request, 'agents.html', {'encabezado':"Team", "agents":agents})