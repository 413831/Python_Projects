from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    # mensajes = {
    #     'msg1': 'Valor mensaje 1',
    #     'msg2': 'Valor mensaje 2'
    # }
    # return render(request, 'bienvenido.html', mensajes)
    numero_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    # personas = Persona.objects.order_by('-id') Forma descendente
    personas = Persona.objects.order_by('id', 'nombre')
    return render(request, 'bienvenido.html', {'numero_personas':numero_personas, 'personas':personas})

def despedirse(args):
    return HttpResponse('Despedida desde Django')

def contacto(args):
    return HttpResponse('Email: contacto@mail.com, Tel.: 5521454354')