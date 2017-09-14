from django.contrib import admin
from core.models import bilhete, ocorrencias, locais_de_ocorrencias, informacoes_de_ocorrencia, parecer_pop, servico_interjato, material, material_retorno

 #Register your models here.

admin.site.register(bilhete)
admin.site.register(ocorrencias)
admin.site.register(locais_de_ocorrencias)
admin.site.register(informacoes_de_ocorrencia)
admin.site.register(parecer_pop)
admin.site.register(servico_interjato)
admin.site.register(material)
admin.site.register(material_retorno)
