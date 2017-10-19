from django.forms import ModelForm
from core.models import bilhete, ocorrencias, locais_de_ocorrencias, informacoes_de_ocorrencia, parecer_pop, servico_interjato, material, material_retorno


class bilhete(ModelForm):
    class Meta:
        model = bilhete
        fields = ['abertura_do_bilhete', 'fechamento_do_bilhete', 'tipo_de_atendimento', 'dias_fechamento', 'horas_fechamento', 'encerramento_do_bilhete', 'dias_de_encerramento', 'status', 'pendencia', 'numero_do_bilhete']


class ocorrencia(ModelForm):
    class Meta:
        model = ocorrencias
        fields = ['protocolo_interjato', 'atendente_interjato', 'id_bilhete']

class locais_de_ocorrencias(ModelForm):
    class Meta:
        model = locais_de_ocorrencias
        fields = ['id_bilhete', 'endereco', 'cidade', 'trecho', 'maps']


class informacoes_de_ocorrencia(ModelForm):
    class Meta:
        model = informacoes_de_ocorrencia
        fields = ['tipo_de_ocorrencia', 'manutencao', 'derivacao_de_ocorrencia', 'responsavel_pelo_rompimento', 'cabo', 'resumo_da_ocorrencia', 'mais_informacoes', 'id_bilhete']


class parecer_pop(ModelForm):
    class Meta:
        model = parecer_pop
        fields = ['id_bilhete', 'fiscal_campo', 'parecer_campo', 'fiscal_administrativo', 'parecer_adm']


class servico_interjato(ModelForm):
    class Meta:
        model = servico_interjato
        fields = ['id_bilhete', 'equipe_de_lancamento', 'equipe_de_fusao', 'tecnico_de_medicao', 'supervisor', 'tempo', 'postes_envolvidos', 'data_de_inicio', 'data_fim', 'tempo_decorrido', 'resumo_do_servico']


class material(ModelForm):
    class Meta:
        model = material
        fields = ['id_bilhete', 'objetos', 'fabricante', 'tipo', 'bandejas', 'fibras', 'derivacoes', 'poste']


class material_retorno(ModelForm):
    class Meta:
        model = material_retorno
        fields = ['id_bilhete', 'objeto_retorno', 'estado']
