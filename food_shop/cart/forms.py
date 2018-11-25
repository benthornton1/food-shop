from django import forms
from food.models import Food

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

class CartAddFromRecipeForm(forms.Form):
	recipe_url = forms.CharField(label = 'Recipe Url:', max_length=200)

