from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from recipes.models import Food
from recipes.forms import RecipeForm
from recipes_user.models import RecipeUser

def index(request):
    html = "index.html"
    data = Food.objects.all()
    context = {"data": data}
    return render(request, html, context)

def recipe(request):
    html = "recipe.html"
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Food.object.create(
                food_title=data['food_title'],
                ingredients=data['ingredients'],
                directions=data['directions'],
                food_author=data['food_image']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, html, context)

def recipedetail(request, username):
    html = "recipe_page.html"
    author = RecipeUser.objects.get(username=username)
    author = request.user
    recipes = Food.objects.filter(food_author=author)
    context = {"author":author, "recipes":recipes}
    return render(request, html, context)

