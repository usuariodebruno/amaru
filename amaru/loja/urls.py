from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    #path('produto/<int:produto_id>/', views.detalhes, name='detalhes'),
]