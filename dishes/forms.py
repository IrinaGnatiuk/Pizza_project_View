from django.forms import ModelForm
from dishes.models import Ingredient
from django import forms


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'is_vegan', 'is_meat', 'price']
        # fields = "__all__"
    name = forms.CharField(required=True, max_length=15)
    price = forms.DecimalField(required=True, max_digits=2)
