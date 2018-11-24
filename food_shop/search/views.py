from django.shortcuts import render
from food.models import Food
# Create your views here.

def search_food(request):
    query =  request.GET.get('search')
    foods = Food.objects.filter(available=True)
    cart_food_form = CartAddProductForm()
    foods = foods.filter(title__icontains=query)
    context = {'genre':genre,'genres':genres,'books':books,'cart_book_form': cart_book_form, 'query':query}
    if len(food)>0:
        return render(request,"search.html",context)
    else:
        context = locals()
        return render(request,"noresults.html",context)
