# Generated by Django 3.2.6 on 2022-08-07 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NASA', '0004_alter_usuario_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gastos_Variable_almacen',
            fields=[
                ('id_gasto_variable_a', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.IntegerField()),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gastos_Variable_linea',
            fields=[
                ('id_gasto_variable_l', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.IntegerField()),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]