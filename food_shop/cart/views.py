from django.shortcuts import render

# Create your views here.
@require_POST
def cart_add(request,food_id):
	cart = Cart(request)