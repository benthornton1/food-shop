from django.urls import path
from . import views

urlpatters = [
	url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<book_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<book_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^clear/$', views.cart_clear, name='cart_clear'),
]