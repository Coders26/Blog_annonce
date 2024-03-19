from django.urls import path

from . import views

urlpatterns = [
    path('new_annonce/', views.new_annonce, name='new_annonce'),
    path('annonce/<int:pk>/details', views.annonce_single, name='annonce_single'),
    path('', views.annonce, name="annonce"),
]