from django import forms

from recipes.models import Food
from recipes_user.models import RecipeUser

class RecipeForm(forms.Form):
    food_title = forms.CharField(max_length=50)
    ingredients = forms.CharField(widget=forms.Textarea)
    directions = forms.CharField(widget=forms.Textarea)
    food_author = forms.ModelChoiceField(queryset=RecipeUser.objects.all())