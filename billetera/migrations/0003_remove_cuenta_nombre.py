# Generated by Django 4.1.5 on 2023-01-19 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billetera', '0002_cuenta_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='nombre',
        ),
    ]
