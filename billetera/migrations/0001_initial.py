# Generated by Django 4.1.5 on 2023-01-19 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=100)),
                ('monto', models.IntegerField()),
                ('tipo', models.CharField(max_length=8)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billetera.cuenta')),
            ],
        ),
    ]