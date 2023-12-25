from django.forms import ModelForm
from django import forms
from .models import UnderContractBuyer, TCdates#, ExtraInfo


class BuyerForm(ModelForm):
	"""docstring for BuyerForm"""
	class Meta:
		model = UnderContractBuyer
		fields = ['team','agent','address','buyer_firstname','buyer_lastname','buyer_email', 'buyer_phone',
		'efective','closing', 'escrow_time','inspection_time','loan_time',
		'titlecompany','titleagent','titlecompany_address','titlecompany_email', 'titlecompany_phone',
		'screenshot', 'other_agent','other_agent_phone','other_agent_email','other_agent_company',
		'price','escrow_amount', 'mls_fee','commission',
		'inspectionteam','inspectionteam_email','inspectionteam_phone', "insurance",
		"financing",'lender','lender_phone','lender_email',
		"thereis_HOA","HOA","HOA_phone", "HOA_email"]
		








		


class TCdatesForm(ModelForm):
	"""docstring for TCdatesForm"""
	class Meta:
		model = UnderContractBuyer
		fields = ['address','efective','closing','escrow_time','inspection_time','loan_time']


'''class ExtraInfoForm(ModelForm):
	"""docstring for ExtraInfoForm"""
	class Meta:
		model = ExtraInfo
		fields = '__all__'
		
		

class LenderForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = ['category', 'lender', 'email', 'phone','company','lender_nmls', 'company_nmls'  ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['category'] = 'Lender'
        self.fields['lender'].widget = forms.TextInput()  # Show a regular text input for lender field
        self.fields['lender_nmls'].widget = forms.TextInput()  # Show a regular text input for lender_nmls field
        self.fields['company_nmls'].widget = forms.TextInput()  # Show a regular text input for company_nmls field

        # Hide the irrelevant fields for category other than 'Lender'
        if self.initial['category'] != 'Lender':
            self.fields['lender'].widget = forms.HiddenInput()
            self.fields['lender_nmls'].widget = forms.HiddenInput()
            self.fields['company_nmls'].widget = forms.HiddenInput()'''


'''class AgentForm(ModelForm):
	class Meta:
		model = UnderContractBuyer
		fields = ['other_agent','other_agent_phone','other_agent_email','other_agent_company']'''
	