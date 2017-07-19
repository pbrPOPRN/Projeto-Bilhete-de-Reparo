# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170622_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='id',
        ),
        migrations.AddField(
            model_name='horario',
            name='atendente_interjato',
            field=models.CharField(default='joao', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horario',
            name='numero_do_bilhete',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horario',
            name='protocolo_interjato',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='horario',
            name='status',
            field=models.CharField(choices=[(' ', 'Pendente'), (' ', 'Fechado'), (' ', 'Finalizado')], max_length=50),
        ),
        migrations.AlterField(
            model_name='horario',
            name='tipo_de_atendimento',
            field=models.CharField(choices=[(' ', 'Trecho sem redundancia fisica'), (' ', 'Trecho com redundancia fisica'), (' ', 'Trecho com atendimento critico')], max_length=50),
        ),
    ]