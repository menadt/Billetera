# Generated by Django 4.1.5 on 2023-01-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billetera', '0004_alter_movimiento_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='tipo',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], max_length=15),
        ),
    ]