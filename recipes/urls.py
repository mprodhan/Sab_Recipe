from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe_add/', views.recipe, name='recipe_add'),
    path('recipe/', views.recipe_page, name='recipe')
]