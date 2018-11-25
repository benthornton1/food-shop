from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cart'
urlpatterns = [
	#path('', views.cart_detail, name='cart_detail'),
    path(r'add/<food_id>/', views.cart_add, name='cart_add'),
    path(r'readd/<order_id>/', views.cart_readd, name='cart_readd'),
    path(r'remove/<food_id>/', views.cart_remove, name='cart_remove'),
    path(r'clear/', views.cart_clear, name='cart_clear'),
    path('', views.get_recipe_url, name='cart_detail'),
]
