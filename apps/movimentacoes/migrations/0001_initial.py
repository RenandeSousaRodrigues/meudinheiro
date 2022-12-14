# Generated by Django 4.1.1 on 2022-09-05 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=70, verbose_name='Descrição')),
                ('discriminacao', models.TextField(blank=True, null=True, verbose_name='Discriminação')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Valor R$')),
                ('anexo', models.FileField(blank=True, null=True, upload_to='anexos', verbose_name='Upload Anexo')),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Data criação')),
                ('data_alteracao', models.DateTimeField(auto_now_add=True, verbose_name='Data Alteração')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='geral.categoria', verbose_name='Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
    ]
