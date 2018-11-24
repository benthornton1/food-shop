from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path(r'^$', views.cart_detail, name='cart_detail'),
    path(r'^add/(?P<book_id>\d+)/$', views.cart_add, name='cart_add'),
    path(r'^remove/(?P<book_id>\d+)/$', views.cart_remove, name='cart_remove'),
    path(r'^clear/$', views.cart_clear, name='cart_clear'),
]