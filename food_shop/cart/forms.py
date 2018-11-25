from django import forms
from food.models import Food




class CartAddProductForm(forms.Form):

    quantity = forms.IntegerField(min_value=1, max_value=2000)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class CartAddFromRecipeForm(forms.Form):
	recipe_url = forms.CharField(label = 'Recipe Url:', max_length=200)

