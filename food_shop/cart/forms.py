from django import forms
from food.models import Food




class CartAddProductForm(forms.Form):

    quantity = forms.IntegerField(min_value=1, max_value=2000)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
