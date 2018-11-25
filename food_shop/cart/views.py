from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from food.models import Food
from order.models import OrderItem
from .cart import Cart
from .forms import CartAddProductForm, CartAddFromRecipeForm
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


def cart_readd(request, order_id):
    cart = Cart(request)
    order_items = OrderItem.objects.filter(order_id = order_id)
    if len(order_items) > 0:
        for item in order_items:
            cart.add(food=item.food,
                    quantity=item.quantity)
    return redirect('cart:cart_detail')



"""
def cart_add_from_recipe(request, web_url):
    cart = Cart(request)
    scraper = scrape_me(web_url)
    ingredients = scraper.ingredients()
    for ing in ingredients:
        query = Food.objects.filter(name=ing)
        if len(query) > 0:
            food = get_object_or_404(Food,id=query[0].id)
            cart.add(food=food,quantity=1,update_quantity=false)
    return redirect('cart:cart_detail')
"""

def get_recipe_url(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})

    if request.method == "POST":
        form = CartAddFromRecipeForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            cd = form.cleaned_data
            url = cd['recipe_url']
            scraper = scrape_me(url)
            ingredients = scraper.ingredients()
            print(ingredients)
            for ing in ingredients:
                words = ing.split(" ")
                for word in words:
                    query = Food.objects.filter(name=word)
                    
                    if len(query) > 0:
                        cur_food = food=query[0]
                        cart.add(food=cur_food)

            
            return render(request,'cart/detail.html', { 'recipe_url_form':form })
    else:
        form = CartAddFromRecipeForm()

    return render(request,'cart/detail.html', { 'recipe_url_form':form })

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
