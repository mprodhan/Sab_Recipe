from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HtttpResponse
from recipes.models import Food
from recipes.forms import RecipeForm
from recipes_user.models import RecipeUser

def index(request):
    html = "index.html"
    return render(request, html)

