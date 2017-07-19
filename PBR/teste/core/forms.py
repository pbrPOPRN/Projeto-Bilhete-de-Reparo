from django.forms import ModelForm
from core.models import bilhete, ocorrencias, locais_de_ocorrencias, informacoes_de_ocorrencia, parecer_pop, servico_interjato, material, material_retorno


class bilhete(ModelForm):
    class Meta:
        model = bilhete
        fields = ['abertura_do_bilhete', 'fechamento_do_bilhete', 'tipo_de_atendimento', 'dias_fechamento', 'horas_fechamento', 'encerramento_do_bilhete', 'dias_de_encerramento', 'status', 'pendencia', 'numero_do_bilhete']


class ocorrencias(ModelForm):
    class meta:
        model = ocorrencias
        fields = ['protocolo_interjato', 'atendente_interjato', 'id_bilhete']

class locais_de_ocorrencias(ModelForm):
    class meta:
        model = locais_de_ocorrencias
        field = ['id_ocorrencia', 'endereco', 'cidade', 'trecho', 'maps',]


class informacoes_de_ocorrencia(ModelForm):
    class meta:
        model = informacoes_de_ocorrencia
        fields = ['tipo_de_ocorrencia', 'manutencao', 'derivacao_de_ocorrencia', 'responsavel_pelo_rompimento', 'cabo', 'resumo_da_ocorrencia', 'mais_informacoes', 'id_ocorrencia',]


class parecer_pop(ModelForm):
    class meta:
        model = parecer_pop
        field = ['id_ocorrencia', 'fiscal_campo', 'parecer_campo', 'fiscal_administrativo', 'parecer_adm',]


class servico_interjato(ModelForm):
    class meta:
        model = servico_interjato
        field = ['id_servico', 'equipe_de_lancamento', 'equipe_de_fusao', 'tecnico_de_medicao', 'supervisor', 'tempo', 'postes_envolvidos', 'data_de_inicio', 'data_fim', 'tempo_decorrido', 'resumo_do_servico',]


class material(ModelForm):
    class meta:
        model = material
        field = ['id_servico', 'objetos', 'fabricante', 'tipo', 'bandejas', 'fibras', 'derivacoes', 'poste']


class retorno(ModelForm):
    class meta:
        field = ['id_servico', 'objeto', 'estado']
