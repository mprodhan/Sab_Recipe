from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from auth.forms import LoginForm, SignUpForm
from recipes_user.models import RecipeUser

def signup_view(request):
    html = "signup.html"
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, html, context)

def login_view(request):
    html = "login.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, html, context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
