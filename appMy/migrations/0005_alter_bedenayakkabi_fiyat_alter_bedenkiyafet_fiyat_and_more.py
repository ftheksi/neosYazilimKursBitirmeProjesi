# Generated by Django 4.1.5 on 2023-04-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_alter_shopbasket_price_all'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedenayakkabi',
            name='fiyat',
            field=models.FloatField(default=0, verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='bedenkiyafet',
            name='fiyat',
            field=models.FloatField(default=0, verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='shopbasket',
            name='price_all',
            field=models.FloatField(default=0, verbose_name='Toplam Fiyat'),
        ),
    ]
