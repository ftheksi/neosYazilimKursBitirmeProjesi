# Generated by Django 4.1.5 on 2023-04-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_alter_bedenayakkabi_fiyat_alter_bedenkiyafet_fiyat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedenayakkabi',
            name='fiyat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='bedenkiyafet',
            name='fiyat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='shopbasket',
            name='price_all',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Fiyat'),
        ),
    ]
