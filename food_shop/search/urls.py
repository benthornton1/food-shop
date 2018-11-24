urlpatterns = [
	url(r'^searchfoods/$', views.search_food, name='search_food'),
	url(r'^filter/$', views.filter, name='filter'),

]
