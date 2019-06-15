# Generated by Django 2.2.2 on 2019-06-15 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('recurso', '0002_auto_20190615_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('identificador', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Identificador')),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True, verbose_name='Solicitado em')),
                ('data_reserva', models.DateTimeField(verbose_name='Reservado para')),
                ('tempo_alocacao', models.PositiveIntegerField(verbose_name='Tempo de alocação')),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recurso.Recurso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Usuario')),
            ],
        ),
    ]
