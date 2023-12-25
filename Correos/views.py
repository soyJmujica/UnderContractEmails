from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.utils import timezone
from .models import UnderContractBuyer, TCdates#, ExtraInfo
from .forms import BuyerForm, TCdatesForm#, ExtraInfoForm, AgentForm
from reportlab.pdfgen import canvas
from django.views.generic import ListView
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
# Create your views here.

def undercontract(request):
	if request.method == 'POST':
		form = BuyerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('transacciones')
	else:
		form = BuyerForm()
	return render(request, "undercontract.html", {'form':form,
		'encabezado':"Under Contract Buyer"})

	'''if request.method == 'GET':
		return render(request, "undercontract.html", {'encabezado':"Under Contract",
		'form':BuyerForm})
	else:
		form = BuyerForm(request.POST, request.FILES)
		new_buyer = form.save(commit=False)
		new_buyer.save()
		return redirect('transacciones')'''

'''def workingwith(request, property_id):
		
	if request.method == 'POST':
		address = get_object_or_404(UnderContractBuyer, pk = property_id)
		form = AgentForm(request.POST, initial = {'category':"Realtor"})
		if form.is_valid():
			other_agent = form.save(commit=True)
			address.other_agent = other_agent
			address.save()
			other_agent.save()
			return redirect('realtors')

	else:
		form = AgentForm(initial = {'category':'Realtor'})
	return render(request, 'workingwith.html', {'form':form, 'encabezado':'Agent Working With'})
'''


def dates(request):
	if request.method == 'GET':
		return render(request,"tcdates.html", {'encabezado': 'TC dates',
			'form':TCdatesForm})
	else:
		form = TCdatesForm(request.POST)
		new_date = form.save(commit=False)
		new_date.save()
		return redirect('transacciones')



'''def extra(request):
	if request.method == "GET":
		return render(request, "extrainfo.html", {'encabezado':"Lender & Insurance",
			'form':ExtraInfoForm})
	else:
		form = ExtraInfoForm(request.POST)
		new_data = form.save(commit=False)
		new_data.save()
		if new_data.category == "Insurance":
			return redirect('insurance')
		elif new_data.category == "Realtor":
			return redirect('realtors')
		elif new_data.category == "Lender":
			return redirect('lenders')

def realtors(request):
	realtors = ExtraInfo.objects.filter(category = "Realtor")
	return render(request, 'realtor.html', {'encabezado':'Realtors', 'realtors':realtors})
def lenders(request):
	lenders = ExtraInfo.objects.filter(category = "Lender")
	return render(request, 'lender.html', {'encabezado':'Lenders', 'Lenders':lenders})
def insurance(request):
	insurances = ExtraInfo.objects.filter(category = "Insurance")
	return render(request, 'insurance.html', {'encabezado':"Insurance", 'insurances':insurances})
	pass'''

def home(request):
	return render(request, "home.html", {'encabezado':"Home"})



def transactions(request):
	filtro = request.GET.get('filtro',)
	if filtro == 'Enviado':
		properties = UnderContractBuyer.objects.filter(emailsend = True)
	elif filtro == 'No Enviado':
		properties = UnderContractBuyer.objects.filter(emailsend = False)
	else:
		properties = UnderContractBuyer.objects.all()
	return render(request, 'transacciones.html',{'encabezado':'Transactions','properties':properties})



def details(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk = property_id)
	
	return render(request, 'detalles.html', {'property': address,
		'encabezado':address.address})



def emails(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk=property_id)
	return render(request, '7correos.html',{'encabezado':address.address, 'property':address})

def closed(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk = property_id)

	return render(request, 'closed.html', {'encabezado':address.address,
		'property':address})



def congratulations(request):
	return render(request, 'correo.html',{

		})


def congratulations_send(mail):
	template = render_to_string('congratulations.html',{'property':mail})
	content = template
	image_path1 = 'static/img/email signature - new.png'
	image_path2 = mail.screenshot.url[1:]
		
	email = EmailMultiAlternatives(
					subject = f"Congratulations!! We are under contract on {mail.address}",
					body = '',
					from_email = settings.EMAIL_HOST_USER,
					to = [mail.buyer_email],
					cc = []
			
					)
	email.attach_alternative(content, 'text/html')

	with open(image_path1, 'rb') as f1:
		img1 = f1.read()
	email.attach(image_path1, img1, 'image/png')
	email.attach('image1_cid',img1,'image/png')
	email.mixed_subtype = 'related'

	with open(image_path2, 'rb') as f2:
		img2 = f2.read()
	email.attach(image_path2, img2, 'image/jpeg')
	email.attach('image2_cid',img2, 'image/jpeg')
	email.mixed_subtype = 'related'




	email.send()



	

def emailsend(request, property_id):
	address = get_object_or_404(UnderContractBuyer, pk = property_id)

	if request.method == 'GET':
		mail = address
		print("Enviando correo")
		congratulations_send(mail)
		print('Congratulations enviado')
	return render(request, 'detalles.html', {'encabezado':address.address,
		'property':address})

