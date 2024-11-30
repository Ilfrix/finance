# Generated by Django 3.2.16 on 2024-11-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wallet',
            options={'verbose_name': 'Кошелек', 'verbose_name_plural': 'Кошельки'},
        ),
        migrations.AlterField(
            model_name='wallet',
            name='card',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Карта'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='cash',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Наличные'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='deposit',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Депозит'),
        ),
    ]
