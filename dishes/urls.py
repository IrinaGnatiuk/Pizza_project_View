from django.conf.urls import url, include
from django.urls import path
from .views import *


urlpatterns = [
    path('dishes/', DishView.as_view()),
    path('', StartView.as_view()),
    path('ingredients/', IngredientView.as_view()),
    path('drinks/', DrinkView.as_view()),
    path('ingredients/new', MakeIngredient.as_view(), name='ingredient_form'),
]