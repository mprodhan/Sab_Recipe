from django.urls import path
from auth import views

urlpatterns = [
    path('signup/', views.signup_view, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]