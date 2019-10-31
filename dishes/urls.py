from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.DishView.as_view()),
    path('ingredients/', views.IngredientView.as_view()),
    path('drinks/', views.DrinkView.as_view()),

]