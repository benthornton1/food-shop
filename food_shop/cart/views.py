from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from food.models import Food
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
       
            for ing in ingredients:
                words = ing.split(" ")
                for word in words:
                    query = Food.objects.filter(name=word)
                    if len(query) > 0:
                        cur_food = food=query[0]
                        cart.add(cur_food)

            
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
