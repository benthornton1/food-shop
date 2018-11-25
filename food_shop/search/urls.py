from django.urls import path

from . import views

app_name='search'
urlpatterns = [
	path('searchfoods/', views.search_food, name='search_food'),
	#url(r'^filter/$', views.filter, name='filter'),

]
