from django.contrib import admin
from core.models import bilhete, atendimento, local, parecer, informacao_servico, material, material_retorno

 #Register your models here.

admin.site.register(bilhete)
admin.site.register(atendimento)
admin.site.register(local)
admin.site.register(informacao_servico)
admin.site.register(parecer)
admin.site.register(material)
admin.site.register(material_retorno)
