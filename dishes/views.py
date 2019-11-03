from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
from django.views.generic.edit import FormView
from dishes.models import Dish, Drink, Ingredient
from django.http import HttpResponse
from .forms import IngredientForm
from django.forms import ModelForm


class DishView(TemplateView):
    model = Dish
    context_object_name = 'dish'
    template_name = 'dishes/dishes.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(DishView, self).get_context_data(**kwargs)
        # context = Order.objects.filter(price__gt=50).order_by('-price')
        context['user_profile'] = Dish.objects.all()
        context['my_var'] = 'TemplateView'
        return context


class DrinkView(ListView):
    model = Drink
    template_name = 'dishes/drinks.html'
    queryset = Drink.objects.order_by("-date_create")
    context_object_name = 'drink'

    def get_quertyset(self):
        return Drink.objects.all()


class IngredientView(View):
    model = Ingredient
    context_object_name = 'ingredient'
    template_name = 'dishes/ingredients.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse("INGREDIENTS!!!")


class StartView(TemplateView):
    model = Ingredient
    context_object_name = 'ingredient'
    template_name = 'dishes/start.html'


class MakeIngredient(FormView):
    model = Ingredient
    template_name = 'dishes/ingredients.html'
    success_url = '/'
    form_class = IngredientForm

    def form_valid(self, form_class):
        Ingredient.objects.create(**form_class.cleaned_data)
        return super().form_valid(form_class)

    def form_invalid(self, form_class):
        print("Some problems")
        return super().form_invalid(form_class)


