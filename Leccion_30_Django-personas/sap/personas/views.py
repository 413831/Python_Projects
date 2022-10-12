from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def ver_detalle(request, id):
    # Se obtiene el objeto del id indicado
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona':persona})

# PersonaForm = modelform_factory(Persona, exclude=[])

def cargar_persona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = PersonaForm()
    # En los casos que sea la primera vez que navega o el formulario es inválido
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})


def editar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            # La función save funcionará como un update a nivel de db
            formaPersona.save()
            return redirect('inicio')
    else:

        formaPersona = PersonaForm(instance=persona)
    # En los casos que sea la primera vez que navega o el formulario es inválido
    return render(request, 'personas/editar.html', {'formaPersona':formaPersona})

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')
