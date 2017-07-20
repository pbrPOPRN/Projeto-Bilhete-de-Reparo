# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170622_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='bandejas',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='data_de_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='horario',
            name='data_fim',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='derivacoes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='equipe_de_fusao',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='equipe_de_lancamento',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='fabricante',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='fibras',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='fiscal_administrativo',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='fiscal_de_campo',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='objetos',
            field=models.CharField(choices=[(' ', 'Cabo'), (' ', 'Caixa de emenda')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='parecer_de_campo',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='perecer_adm',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='poste',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='postes_envolvidos',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='resumo_do_servico',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='supervisor',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='tecnico_de_medicao',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='tempo',
            field=models.CharField(choices=[(' ', 'Aberto'), (' ', 'Chuvoso'), (' ', 'Nublado')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='tempo_decorrido',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='horario',
            name='tipo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='atendente_interjato',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='cabo',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='cidade',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='derivacao_de_ocorrencia',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='dias_de_encerramento',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='dias_fechamento',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='encerramento_do_bilhete',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='endereco',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='fechamento_do_bilhete',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horas_fechamento',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='mais_informacoes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='manutencao',
            field=models.CharField(choices=[(' ', 'Corretiva'), (' ', 'Preventiva'), (' ', 'Programada')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='maps',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='pendencia',
            field=models.TextField(default='----'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='protocolo_interjato',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='responsavel_pelo_rompimento',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='resumo_da_ocorrencia',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='status',
            field=models.CharField(choices=[(' ', 'Pendente'), (' ', 'Fechado'), (' ', 'Finalizado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='tipo_de_atendimento',
            field=models.CharField(choices=[(' ', 'Trecho sem redundancia fisica'), (' ', 'Trecho com redundancia fisica'), (' ', 'Trecho com atendimento critico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='tipo_de_ocorrencia',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='trecho',
            field=models.CharField(max_length=60, null=True),
        ),
    ]