from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from core.models import bilhete, atendimento, local, parecer, informacao_servico, material, material_retorno


class bilhetes(ModelForm):
    class Meta:
        model = bilhete
        fields = '__all__'


class atendimento(ModelForm):
    class Meta:
        model = atendimento
        fields = '__all__'
        exclude=['id_bilhete']

class local(ModelForm):
    class Meta:
        model = local
        exclude=['id_bilhete']    
        fields = '__all__'

class informacao_servico(ModelForm):
    class Meta:
        model = informacao_servico
        exclude=['id_bilhete']    
        fields = '__all__'

class parecer(ModelForm):
    class Meta:
        model = parecer
        exclude=['id_bilhete']
        fields = '__all__'

class material(ModelForm):
    class Meta:
        model = material
        exclude=['id_bilhete']
        fields = '__all__'


class material_retorno(ModelForm):
    class Meta:
        model = material_retorno
        exclude=['id_bilhete']
        fields = '__all__'