# Generated by Django 4.2.20 on 2025-04-07 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_tipotreinamento_grupotreinamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupotreinamento',
            name='tipotreinamento',
        ),
        migrations.DeleteModel(
            name='TipoTreinamento',
        ),
    ]
