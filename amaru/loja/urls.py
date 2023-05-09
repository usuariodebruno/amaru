from django.contrib import admin
from django.urls import path
import loja.urls
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    #path('produto/<int:produto_id>/', views.detalhes, name='detalhes'),
]