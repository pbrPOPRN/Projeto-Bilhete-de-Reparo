from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.utils import timezone



STATUS_CHOICES = (
    ('Pendente', 'Pendente'),
    ('Fechado', 'Fechado'),
    ('Finalizado', 'Finalizado')


)

ATENDIMENTO_CHOICES = (
    ('TSRF', 'Trecho sem redundancia fisica'),
    ('TCRF', 'Trecho com redundancia fisica'),
    ('TCAT', 'Trecho com atendimento critico')

)

MANUTENCAO_CHOICES = (('corretiva', 'Corretiva'), ('Preventiva', 'Preventiva'), ('Programada', 'Programada'))

TEMPO_CHOICES = (
    ('aberto', 'Aberto'),
    ('chuvoso', 'Chuvoso'),
    ('nublado', 'Nublado')

)
OBJETOS_CHOICES = ((' ', 'Cabo'),(' ', 'Caixa de emenda'))

class bilhete(models.Model):

    abertura_do_bilhete = models.DateTimeField(default=timezone.now)
    fechamento_do_bilhete = models.DateTimeField(null=True)
    tipo_de_atendimento = models.CharField(max_length=50, choices=ATENDIMENTO_CHOICES, null=True)
    slaDias_fechamento = models.IntegerField(null=True)
    slaHoras_fechamento = models.TimeField(null=True)
    slaEncerramento = models.DateField("encerramento", null=True)
    slaDias_de_encerramento = models.IntegerField(null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True)
    pendencia = models.TextField(default='----')
    flagModerador = models.TextField(default='----')
    msgModerador = models.IntegerField(null = True)


#DEFAULT_BILHETE = bilhete.objects.latest('numero_do_bilhete')
class atendimento(models.Model):

    id_bilhete = models.OneToOneField('bilhete', on_delete=models.CASCADE)
    protocoloEmp = models.CharField(max_length=60, null=True)
    atendenteEmp = models.CharField(max_length=60, null=True)
    causaOcorrencia = models.TextField(default="--")
    tipoManutencao = models.CharField("Tipo de ocorrencia",max_length=60, null=True)
    

    def save(self, *args, **kwargs):
        self.id_bilhete = bilhete.objects.latest('id')
        super(atendimento, self).save(*args, **kwargs)


class local(models.Model):

    id_bilhete = models.OneToOneField('bilhete', on_delete=models.CASCADE)
    endereco = models.CharField(max_length=60, null=True)
    cidade = models.CharField(max_length=60, null=True)
    trecho = models.CharField(max_length=60, null=True)
    localizacao = models.CharField(max_length=60, null=True)
    pontoA = models.IntegerField()
    pontoB = models.IntegerField()
    

    def save(self, *args, **kwargs):
        self.id_bilhete = bilhete.objects.latest('id')
        super(local, self).save(*args, **kwargs)


class informacao_servico(models.Model):
    id_bilhete = models.OneToOneField('bilhete', on_delete=models.CASCADE)
    manutencao = models.CharField(max_length=50, choices=MANUTENCAO_CHOICES, null = True)
    derivacao_de_ocorrencia = models.CharField(max_length=60, null=True)
    responsavel_pelo_rompimento = models.CharField(max_length=60, null=True)
    cabo = models.CharField(max_length=60, null=True)
    resumo_da_ocorrencia = models.CharField(max_length=60, null=True)
    mais_informacoes = models.TextField(null=True)
    equipeLancamento = models.CharField(max_length=60, null=True)
    equipeFusao = models.CharField(max_length=60, null=True)
    tecnicoMedicao = models.CharField(max_length=60, null=True)
    supervisor = models.CharField(max_length=60, null=True)
    tempo = models.CharField("Tempo",max_length=50, choices=TEMPO_CHOICES, null=True)
    postesEnv = models.CharField(max_length=60, null=True)
    data_de_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(null=True)
    tempo_decorrido = models.TimeField(null=True)
    resumo_do_servico = models.TextField(null=True)
    

    def save(self, *args, **kwargs):
        self.id_bilhete = bilhete.objects.latest('id')
        super(informacao_servico, self).save(*args, **kwargs)


class parecer(models.Model):

    id_bilhete = models.OneToOneField('bilhete', on_delete=models.CASCADE)
    fiscal_campo = models.CharField("fiscal de campo", max_length=60, null=True)
    parecer_campo = models.CharField("parecer de campo", max_length=60, null=True)
    fiscal_administrativo = models.CharField("fiscal administrativo", max_length=60, null=True)
    parecer_adm = models.CharField("parecer administrativo", max_length=60, null=True)


    def save(self, *args, **kwargs):
        self.id_bilhete = bilhete.objects.latest('id')
        super(parecer, self).save(*args, **kwargs)

class material(models.Model):    # material envolvido
    id_bilhete = models.OneToOneField('bilhete', on_delete=models.CASCADE)
    objetos = models.CharField(max_length=50, choices=OBJETOS_CHOICES , null=True)
    fabricante = models.CharField(max_length=50, null=True)
    tipo = models.CharField(max_length=50, null=True)
    bandejas = models.IntegerField(null=True)
    fibras = models.IntegerField(null=True)
    derivacoes = models.IntegerField(null=True)
    poste = models.CharField(max_length=50, null=True)
    

    def save(self, *args, **kwargs):
        self.id_bilhete = bilhete.objects.latest('id')
        super(material, self).save(*args, **kwargs)

class material_retorno(models.Model):
    id_bilhete = models.OneToOneField('bilhete', on_delete=models.CASCADE)
    objeto_retorno = models.CharField(max_length = 15, null=True)
    estado = models.CharField(max_length=50, null=True)


    def save(self, *args, **kwargs):
        self.id_bilhete = bilhete.objects.latest('id')
        super(material_retorno, self).save(*args, **kwargs)