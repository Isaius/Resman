# Generated by Django 2.2.2 on 2019-06-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PesquisaRecursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(blank=True, max_length=10)),
                ('descricao', models.CharField(blank=True, max_length=140)),
                ('tipo', models.CharField(blank=True, choices=[('portatil', 'Portátil'), ('nportatil', 'Não Portátil')], max_length=15)),
                ('categoria', models.CharField(blank=True, choices=[('espaco', 'Espaço'), ('acessorio', 'Acessórios'), ('computador', 'Computadores'), ('projetor', 'Projetores'), ('moveis', 'Móveis')], max_length=20)),
                ('estado', models.CharField(blank=True, choices=[('disponivel', 'Disponível'), ('reservado', 'Reservado'), ('indisponivel', 'Indisponível'), ('emprestado', 'Emprestado')], default='disponivel', max_length=20)),
                ('setor', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='id',
        ),
        migrations.AlterField(
            model_name='recurso',
            name='MDI',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='categoria',
            field=models.CharField(choices=[('espaco', 'Espaço'), ('acessorio', 'Acessórios'), ('computador', 'Computadores'), ('projetor', 'Projetores'), ('moveis', 'Móveis')], max_length=20),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='identificador',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='tipo',
            field=models.CharField(choices=[('portatil', 'Portátil'), ('nportatil', 'Não Portátil')], max_length=15),
        ),
    ]
