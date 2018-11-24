from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

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
    return render(request, 'food/detail.html', {'food': food})
