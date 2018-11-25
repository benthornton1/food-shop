from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:food_id>/', views.detail, name='detail'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:cat_name>/', views.view_category, name='view_category'),
]
