from django.shortcuts import render
from food.models import Food
# Create your views here.

def search_food(request):
    query =  request.GET.get('search')
    foods = Food.objects.filter(available=True)
    foods = foods.filter(title__icontains=query)
    context = {'food': food}
    if len(food)>0:
        return render(request,"search.html",context)
    else:
        context = locals()
        return render(request,"no_results.html",context)
