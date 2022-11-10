from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('drinks/', views.drinks_index, name='drinks_index'),
  path('drinks/<int:drink_id>/', views.drinks_detail, name='drinks_detail'),
  path('drinks/create/', views.DrinkCreate.as_view(), name='drink_create'),
]