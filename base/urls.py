from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('newmeal/', views.newMeal, name="newMeal"),
    path('usermeals/', views.userMeals, name="userMeals"),
    path('impact/', views.impact, name="impact"),
    path('about/', views.about, name="about"),
]