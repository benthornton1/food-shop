from django.shortcuts import render
from food.models import Food
# Create your views here.

def search_food(request):
    query =  request.GET.get('search')
    foods = Food.objects.filter(available=True)
    foods = foods.filter(name__icontains=query)
    context = {'food': foods, 'query': query }
    if len(foods)>0:
        return render(request,"search/search.html",context)
    else:
        context = locals()
        return render(request,"search/no_results.html",context)
