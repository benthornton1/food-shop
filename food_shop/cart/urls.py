from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cart'
urlpatterns = [
	path('', views.cart_detail, name='cart_detail'),
    path(r'^add/(?P<food_id>\d+)/$', views.cart_add, name='cart_add'),
    path(r'^remove/(?P<food_id>\d+)/$', views.cart_remove, name='cart_remove'),
    path(r'^clear/$', views.cart_clear, name='cart_clear'),
    path('cart_add_from_recipe/<path:web_url>',views.cart_add_from_recipe,name='cart_add_from_recipe'),
]
