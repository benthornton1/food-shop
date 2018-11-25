from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from django.db.models import Q

from .models import Food

def index(request):
    food_list = Food.objects.order_by('-name')
    template = 'food/index.html'
    context = {
        'food_list': food_list
    }
    return render(request, template, context)

def detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    cart_food_form = CartAddProductForm()
    return render(request, 'food/detail.html', {'food': food, 'cart_food_form': cart_food_form})

def categories(request):
	category_list = Food.objects.order_by('-category').values('category').distinct()
	template = 'food/categories.html'
	context = {
		'category_list': category_list
	}
	return render(request, template, context)

def view_category(request, cat_name):
	food_list = Food.objects.filter(category=cat_name)
	template = 'food/view_cat.html'
	context = {
		'food_list': food_list,
		'category': cat_name,
	}
	return render(request,template,context)
