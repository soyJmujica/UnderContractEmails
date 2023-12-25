from django.db import models
from djmoney.models.fields import MoneyField
from datetime import timedelta
from Team.models import TeamMembers
# Create your models here.


class UnderContractBuyer(models.Model):
	team = models.CharField(max_length = 20,choices = [('Citrus','Citrus'),('Pinellas','Pinellas')])
	agent = models.ForeignKey(TeamMembers, on_delete = models.SET_DEFAULT,default=1)
	status = models.CharField(max_length = 20, choices = [('Pending','Pending'),('Closed','Closed')],
		default = 'Pending')
	address = models.CharField(max_length = 100, verbose_name='Property')
	buyer_firstname = models.CharField(max_length = 100, verbose_name="Buyer's first name")
	buyer_lastname = models.CharField(max_length = 100,verbose_name="Buyer's last name")
	buyer_email = models.CharField(max_length = 100, verbose_name='Email')
	buyer_phone = models.CharField(max_length = 100, verbose_name='Phone number')
	titlecompany = models.CharField(max_length = 100, verbose_name='Title company')
	titleagent = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Title Agent")
	titlecompany_email = models.CharField(max_length = 100,verbose_name="Title's email")
	titlecompany_phone = models.CharField(max_length = 100,verbose_name="Title's phone number")
	titlecompany_address = models.CharField(max_length = 100, verbose_name = "Title Address")
	screenshot = models.ImageField(upload_to = 'title_screenshots/',blank=True,null = True, verbose_name = "Title Company Screenshot")
	price = MoneyField(max_digits = 20, decimal_places = 2, default_currency="USD",verbose_name="Price")
	escrow_amount = MoneyField(max_digits = 10, decimal_places = 2, default_currency = "USD",verbose_name='Escrow')
	mls_fee = MoneyField(max_digits = 10, decimal_places = 2,default_currency = "USD",verbose_name='MLS Fee')
	commission = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Commission')
	inspectionteam = models.CharField(max_length=100, blank = True, verbose_name='Inspection Team')
	inspectionteam_email = models.CharField(max_length = 100, blank = True,verbose_name="Inspection Team's email")
	inspectionteam_phone = models.CharField(max_length = 100, blank = True,verbose_name="Inspection Team's Phone")
	HOA = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "HOA")
	HOA_phone = models.CharField(max_length = 100,blank = True, null = True,verbose_name="HOA Phone")
	HOA_email = models.CharField(max_length = 100,blank = True, null = True, verbose_name="HOA Email")
	emailsend = models.BooleanField(default = False)
	insurance = models.BooleanField(default = True)
	financing = models.CharField(max_length = 100, choices = [('Cash','Cash'),
		('Conventional','Conventional'), ('FHA','FHA'), ('VA','VA'), ('Others','Others')])
	thereis_HOA = models.BooleanField(default = False, verbose_name = "There is HOA")
	created = models.DateTimeField(auto_now_add = True)
	efective = models.DateField(verbose_name='Efective Date')
	closing = models.DateField(verbose_name='Closing Date')
	escrow_time = models.IntegerField(verbose_name='Escrow Time')
	inspection_time = models.IntegerField(verbose_name='Inspection Time')
	loan_time = models.IntegerField(verbose_name='Loan Time')
	escrow_date = models.DateField(blank=True, null=True,verbose_name='Escrow Due Date')
	HOA_date = models.DateField(blank=True, null=True, verbose_name='HOA/Condo Application Due Date')
	inspection_date = models.DateField(blank=True, null=True, verbose_name='Inspection Due Date')
	commitment = models.DateField(blank=True, null=True, verbose_name='Title Commitment Due Date')
	loan_approval = models.DateField(blank=True, null=True, verbose_name='Loan Approval')
	cleartoclose = models.DateField(blank=True, null=True,verbose_name='Clear to Close')
	lien = models.DateField(blank=True, null=True, verbose_name='Lien Search')
	DA_request = models.DateField(blank=True, null=True, verbose_name='DA Request')
	other_agent = models.CharField(max_length = 100, null = True, blank = True, verbose_name = 'Agent Working with')
	other_agent_phone = models.CharField(max_length = 100, null = True, blank = True, verbose_name = "Agent's Phone")
	other_agent_email = models.CharField(max_length = 100, null = True, blank = True, verbose_name = "Agent's Email")
	other_agent_company = models.CharField(max_length = 100, null = True, blank = True, verbose_name = "Agent's company")
	lender = models.CharField(max_length = 100, null = True, blank = True, verbose_name = 'Lender')
	lender_phone = models.CharField(max_length = 100, null = True, blank = True, verbose_name = "Lender's Phone")
	lender_email = models.CharField(max_length = 100, null = True, blank = True, verbose_name = "Lender's Email")
	
	def is_weekday(self, fecha):
		return fecha.weekday() >= 5

	def save(self, *args, **kwargs):
		self.screenshot.name = str(self.titlecompany+'.jpg')
		self.escrow_date = self.efective + timedelta(days=self.escrow_time)
		self.HOA_date = self.efective + timedelta(days= 5)
		self.inspection_date = self.efective + timedelta(days=self.inspection_time)
		diferencia = self.closing-self.efective
		fecha1 = self.closing-timedelta((diferencia.days)/2)
		fecha2 = self.closing-timedelta(days=15)
		fecha1_2 = fecha1+timedelta(days=1)
		fecha2_2 = fecha2+timedelta(days=1)
		if diferencia.days < 30:
			if fecha1.weekday()>=5:
				fecha1 = fecha1
			else:
				if fecha1_2.weekday()>=5:
					fecha1 = fecha1+timedelta(days=1)
				else:
					fecha1 = fecha1-timedelta(days=1)
			self.commitment = fecha1
		else:
			if fecha2.weekday()>=5:
				fecha2=fecha2
			else:
				if fecha2_2.weekday()>=5:
					fecha2 = fecha2+timedelta(days=1)
				else:
					fecha2 = fecha2-timedelta(days=1)
			self.commitment = fecha2

		if diferencia.days < 30:
			if self.loan_time == 0:
				pass
			elif self.loan_time in range(1,31):
				self.loan_approval = self.efective+timedelta(days=self.loan_time)
			else:
				self.loan_approval=self.closing
		else:
			if self.loan_time==0:
				pass

			else:
				self.loan_approval=self.efective+timedelta(days=self.loan_time)

		self.cleartoclose = self.closing - timedelta(days=7)
		self.lien = self.closing - timedelta(days=10)
		self.DA_request = self.inspection_date+timedelta(days=1)

		super().save(*args, **kwargs)


	def hide(self, *args, **kwargs):
		if self.thereis_HOA == False:
			self.HOA = None
			self.HOA_phone = None
			self.HOA_email = None
		super().save(*args, **kwargs)

		"""docstring for TCdates"""
	def __str__(self):
		if self.category in [self.INSURANCE, self.REALTOR]:
			return str(self.agent + " -  " + self.category)

		elif self.category == self.LENDER:
			return str((self.lender+"  -  "+self.category))



	def __str__(self):
		return self.address



	"""docstring for UnderContractBuyer
	def __init__(self, arg):
		super(UnderContractBuyer, self).__init__()
		self.arg = arg"""
		

class TCdates(models.Model):
	address = models.ForeignKey(UnderContractBuyer, on_delete = models.CASCADE,verbose_name='Property')
	efective = models.DateField(verbose_name='Efective Date')
	closing = models.DateField(verbose_name='Closing Date')
	escrow_time = models.IntegerField(verbose_name='Escrow Time')
	inspection_time = models.IntegerField(verbose_name='Inspection Time')
	loan_time = models.IntegerField(verbose_name='Loan Time')
	escrow_date = models.DateField(blank=True, null=True,verbose_name='Escrow Due Date')
	HOA_date = models.DateField(blank=True, null=True, verbose_name='HOA/Condo Application Due Date')
	inspection_date = models.DateField(blank=True, null=True, verbose_name='Inspection Due Date')
	commitment = models.DateField(blank=True, null=True, verbose_name='Title Commitment Due Date')
	loan_approval = models.DateField(blank=True, null=True, verbose_name='Loan Approval')
	cleartoclose = models.DateField(blank=True, null=True,verbose_name='Clear to Close')
	lien = models.DateField(blank=True, null=True, verbose_name='Lien Search')
	DA_request = models.DateField(blank=True, null=True, verbose_name='DA Request')

	def is_weekday(self, fecha):
		return fecha.weekday() >= 5

	def save(self, *args, **kwargs):
		self.escrow_date = self.efective + timedelta(days=self.escrow_time)
		self.HOA_date = self.efective + timedelta(days= 5)
		self.inspection_date = self.efective + timedelta(days=self.inspection_time)
		diferencia = self.closing-self.efective
		fecha1 = self.closing-((diferencia)/2)
		fecha2 = self.closing-timedelta(days=15)
		if diferencia.days < 30:
			if self.is_weekday(fecha1):
				fecha1 = fecha1
			else:
				if self.is_weekday(fecha1+timedelta(days=1)):
					fecha1 = fecha1+timedelta(days=1)
				else:
					fecha1 = fecha1-timedelta(days=1)
			self.commitment = fecha1
		else:
			if is_weekday(fecha2):
				fecha2=fecha2
			else:
				if self.is_weekday(fecha2+timedelta(days=1)):
					fecha2 = fecha2+timedelta(days=1)
				else:
					fecha2 = fecha2-timedelta(days=1)
			self.commitment = fecha2

		if diferencia.days < 30:
			if self.loan_time == 0:
				self.loan_approval=models.CharField()
				self.loan_approval = 'CASH DEAL'
			elif self.loan_time < 30:
				self.loan_approval = self.efective+timedelta(days=self.loan_time)
			else:
				self.loan_approval=self.closing
		else:
			if self.loan_time==0:
				self.loan_approval=models.CharField()
				self.loan_approval = 'CASH DEAL'

			else:
				self.loan_approval=self.efective+timedelta(days=self.loan_time)

		self.cleartoclose = self.closing - timedelta(days=7)
		self.lien = self.closing - timedelta(days=10)
		self.DA_request = self.inspection_date+timedelta(days=1)

		super().save(*args, **kwargs)

	"""docstring for TCdates"""
	def __str__(self):
		return self.address

'''
class ClassName(models.Model):
	category = models.CharField(max_length = 100, choices = [(Lender,"Lender"),
															Insurance, "Insurance"], verbose_name = "Categoria")
	company = models.CharField(max_length = 100, verbose_name = "Company")
	contact = models.CharField(max_length = 100, verbose_name = "Agent")
	phone = models.CharField(max_length = 100, verbose_name = "Phone Number")
	email =  

	"""docstring for ClassName"""
	def __str__(self):
		super(ClassName, self).__init__()
		self.arg = arg
'''		
'''class ExtraInfo(models.Model):
	INSURANCE = 'Insurance'
	LENDER = 'Lender'
	REALTOR = 'Realtor'

	CHOICES = [
		(INSURANCE, 'Insurance'),
		(LENDER, 'Lender'),
		(REALTOR, 'Realtor')
	]

	category = models.CharField(max_length=20, choices=CHOICES)
	company = models.CharField(max_length=100, blank = True, null = True)
	email = models.CharField(max_length = 100)
	phone = models.CharField(max_length=20)

	# Insurance fields
	agent = models.CharField(max_length=100, blank=True, null=True)

	# Lender fields
	lender = models.CharField(max_length=100, blank=True, null=True)
	lender_nmls = models.CharField(max_length=20, blank=True, null=True)
	company_nmls = models.CharField(max_length=20, blank=True, null=True)

	def save(self, *args, **kwargs):
		if self.category in [self.INSURANCE, self.REALTOR]:
			self.lender = None
			self.lender_nmls = None
			self.company_nmls = None
		elif self.category == self.LENDER:
			self.agent = None
		super().save(*args, **kwargs)

		"""docstring for TCdates"""
	def __str__(self):
		if self.category in [self.INSURANCE, self.REALTOR]:
			return str(self.agent + " -  " + self.category)

		elif self.category == self.LENDER:
			return str((self.lender+"  -  "+self.category))'''