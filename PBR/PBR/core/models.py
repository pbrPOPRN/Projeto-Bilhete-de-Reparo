from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.utils import timezone

STATUS_CHOICES = (
    (' ', 'Pendente'),
    (' ', 'Fechado'),
    (' ', 'Finalizado')

)

ATENDIMENTO_CHOICES = (
    (' ', 'Trecho sem redundancia fisica'),
    (' ', 'Trecho com redundancia fisica'),
    (' ', 'Trecho com atendimento critico')

)

MANUTENCAO_CHOICES = ((' ', 'Corretiva'),(' ', 'Preventiva'),(' ', 'Programada'))

TEMPO_CHOICES = (
    (' ', 'Aberto'),
    (' ', 'Chuvoso'),
    (' ', 'Nublado')

)
OBJETOS_CHOICES = ((' ', 'Cabo'),(' ', 'Caixa de emenda'))


class bilhete(models.Model):

    abertura_do_bilhete = models.DateTimeField(default=timezone.now)
    fechamento_do_bilhete = models.DateTimeField(null=True)
    tipo_de_atendimento = models.CharField(max_length=50, choices=ATENDIMENTO_CHOICES, null=True)
    dias_fechamento = models.IntegerField(null=True)
    horas_fechamento = models.TimeField(null=True)
    encerramento_do_bilhete = models.DateField("encerramento", null=True)
    dias_de_encerramento = models.IntegerField(null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True)
    pendencia = models.TextField(default='----')
    numero_do_bilhete = models.AutoField(primary_key=True)




class ocorrencias(models.Model):

    id_bilhete = models.ForeignKey('bilhete', on_delete=models.CASCADE)
    protocolo_interjato = models.CharField(max_length=60, null=True)
    atendente_interjato = models.CharField(max_length=50, null=True)


class locais_de_ocorrencias(models.Model):

    id_bilhete = models.ForeignKey('bilhete', on_delete=models.CASCADE)
    endereco = models.CharField(max_length=60, null=True)
    cidade = models.CharField(max_length=60, null=True)
    trecho = models.CharField(max_length=60, null=True)
    maps = models.CharField(max_length=60, null=True)


class informacoes_de_ocorrencia(models.Model):
    id_bilhete = models.ForeignKey('bilhete', on_delete=models.CASCADE)
    tipo_de_ocorrencia = models.CharField(max_length=60, null=True)
    manutencao = models.CharField(max_length=50, choices=MANUTENCAO_CHOICES, null = True)
    derivacao_de_ocorrencia = models.CharField(max_length=60, null=True)
    responsavel_pelo_rompimento = models.CharField(max_length=60, null=True)
    cabo = models.CharField(max_length=60, null=True)
    resumo_da_ocorrencia = models.CharField(max_length=60, null=True)
    mais_informacoes = models.TextField(null=True)


class parecer_pop(models.Model):

    id_bilhete = models.ForeignKey('bilhete', on_delete=models.CASCADE)
    fiscal_campo = models.CharField("fiscal de campo", max_length=60, null=True)
    parecer_campo = models.CharField("parecer de campo", max_length=60, null=True)
    fiscal_administrativo = models.CharField("fiscal administrativo", max_length=60, null=True)
    parecer_adm = models.CharField("parecer administrativo", max_length=60, null=True)


class servico_interjato(models.Model):

    id_bilhete = models.ForeignKey('bilhete', on_delete=models.CASCADE)
    equipe_de_lancamento = models.CharField(max_length=60, null=True)
    equipe_de_fusao = models.CharField(max_length=60, null=True)
    tecnico_de_medicao = models.CharField(max_length=60, null=True)
    supervisor = models.CharField(max_length=60, null=True)
    tempo = models.CharField(max_length=50, choices=TEMPO_CHOICES, null=True)
    postes_envolvidos = models.CharField(max_length=60, null=True)
    data_de_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(null=True)
    tempo_decorrido = models.TimeField(null=True)
    resumo_do_servico = models.TextField(null=True)


class material(models.Model):    # material envolviodo
    id_bilhete = models.ForeignKey('bilhete', on_delete=models.CASCADE)
    objetos = models.CharField(max_length=50, choices=OBJETOS_CHOICES , null=True)
    fabricante = models.CharField(max_length=50, null=True)
    tipo = models.CharField(max_length=50, null=True)
    bandejas = models.IntegerField(null=True)
    fibras = models.IntegerField(null=True)
    derivacoes = models.IntegerField(null=True)
    poste = models.CharField(max_length=50, null=True)


class material_retorno(models.Model):
    id_bilhete = models.ForeignKey('bilhete', on_delete=models.CASCADE)
    objeto_retorno = models.CharField(max_length = 15, null=True)
    estado = models.CharField(max_length=50, null=True)
