from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from food.models import Food
from .cart import Cart
from .forms import CartAddProductForm
from recipe_scrapers import scrape_me

# Create your views here.
@require_POST
def cart_add(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food=food,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_add_from_recipe(request, web_url):
    cart = Cart(request)
    scraper = scrape_me(web_url)
    ingredients = scraper.ingredients()
    for ing in ingredients:
        query = Food.objects.filter(name=ing)
        if len(query) > 0:
            food = get_object_or_404(Food,id=query[0].id)
            cart.add(food=food,quantity=1,false)
    return redirect('cart:cart_detail')

def cart_remove(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Food, id=food_id)
    cart.remove(food)
    return redirect('cart:cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
