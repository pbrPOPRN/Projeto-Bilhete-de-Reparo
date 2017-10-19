from django.shortcuts import render, redirect
from core.forms import bilhetes, atendimento, local, parecer, informacao_servico, material, material_retorno
from core.models import bilhete

# Create your views here.


def home(request):
    var = '123'
    return render(request, 'core/index.html', {'var': var})


def bilhetef(request):
    formbilhete = bilhetes(request.POST or None)
    atdForm = atendimento(request.POST or None)
    localForm = local(request.POST or None)
    infserForm = informacao_servico(request.POST or None)
    parForm = parecer(request.POST or None)
    matForm = material(request.POST or None)
    matrtrnForm =  material_retorno(request.POST or None)

    if request.POST:

        formbilhete.save()
       # form_bilhete = bilhete.objects.latest()
       # atdForm.save(commit=False)
       # atdForm.id_bilhete = form_bilhete
        atdForm.save()
       # localForm.save(commit=False)
       # localForm.id_bilhete = form_bilhete
        localForm.save()
       # infserForm.save(commit=False)
        #infserForm.id_bilhete = form_bilhete
        infserForm.save()
       # parForm.save(commit=False)
        #parForm.id_bilhete = form_bilhete
        parForm.save()
       # matForm.save(commit=False)
       # matForm.id_bilhete = form_bilhete
        matForm.save()
       # matrtrnForm.save(commit=False)
        #matrtrnForm.id_bilhete = form_bilhete
        matrtrnForm.save()


    return render(request, 'core/formulario.html', {'bilhete': formbilhete, 'atd': atdForm, 'local': localForm, 'infSer': infserForm,'parecer': parForm, 'material': matForm, 'matrtrn':matrtrnForm})
