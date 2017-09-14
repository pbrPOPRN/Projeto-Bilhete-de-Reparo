from django.shortcuts import render, redirect
from core.forms import bilhete, ocorrencia, locais_de_ocorrencias, informacoes_de_ocorrencia, parecer_pop, servico_interjato, material, material_retorno


# Create your views here.


def home(request):
    var = '123'
    return render(request, 'core/index.html', {'var': var})


def bilhetef(request):
    formbilhete = bilhete(request.POST or None)
    formocorre = ocorrencia(request.POST or None)
    formlocalocorre = locais_de_ocorrencias(request.POST or None)
    forminfoocorre = informacoes_de_ocorrencia(request.POST or None)
    formparecerpop = parecer_pop(request.POST or None)
    formserinterj = servico_interjato(request.POST or None)
    formmateriais = material(request.POST or None)
    formmatertrn =  material_retorno(request.POST or None)

    if request.POST:


        formbilhete.save()
        formocorre.save()
        formlocalocorre.save()
        forminfoocorre.save()
        formparecerpop.save()
        formserinterj.save()
        formmateriais.save()
        formmatertrn.save()



    return render(request, 'core/formulario.html', {'bilhete': formbilhete, 'ocorre': formocorre, 'lococorre': formlocalocorre, 'infocorre': forminfoocorre,'parecerpop': formparecerpop, 'servinter': servico_interjato, 'material': formmateriais, 'materialretrn':formmatertrn})
