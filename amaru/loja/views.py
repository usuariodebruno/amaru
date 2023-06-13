from django.http import HttpResponse
from django.shortcuts import render
import random

from django.template import loader
from .models import Produto, Categoria

# Create your views here.

def index(request):
    produtos = Produto.objects.all()    
    template = loader.get_template('loja/index.html')
    context = { #VARIAVAEIS QUE VÃO PARA O TEMPLATES
        'produtos': reversed(produtos),
    }  
    return HttpResponse(template.render(context, request))

