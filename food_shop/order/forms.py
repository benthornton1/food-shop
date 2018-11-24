from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from .models import Order

class OrderCreateForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = ('card_number', 'cardholder_name', 'expiry_date', 'CVV_code')


# Validate card_number field.  Usage def clean_<FIELD NAME >, i.e. attributes from 
# the model used for this form
		
	def clean_card_number(self):
		card_number = self.cleaned_data['card_number']

		#check the user input is only numbers
		if not card_number.isdigit():
			raise forms.ValidationError("Card number can only contain numbers")

		#check the user inputs exactly 16 digits 
		elif len(card_number) != 16:
			raise ValidationError('Card must contain 16 digits')
		
		return card_number


	def clean_CVV_code(self):
		CVV = self.cleaned_data['CVV_code']

		if not CVV.isdigit():
			raise forms.ValidationError("CVV code can only contain numbers")

		elif len(CVV) != 3:
			raise ValidationError("CVV code must contain 3 digits")

		return CVV