# Generated by Django 4.0.5 on 2022-06-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbookapp', '0005_alter_trade_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='fecha',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de operacion (mm/dd/yyyy)'),
        ),
    ]
