from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('', views.authentification, name="authentification"),
    path('logout', views.deconnexion, name="logout"),
]