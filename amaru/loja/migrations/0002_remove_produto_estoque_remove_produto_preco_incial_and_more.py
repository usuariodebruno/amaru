# Generated by Django 4.2.1 on 2023-05-09 03:59

from django.db import migrations, models
import loja.models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='estoque',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='preco_incial',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='vendedor',
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=loja.models.get_default_preco, max_digits=8),
        ),
        migrations.DeleteModel(
            name='Mensagem',
        ),
    ]
