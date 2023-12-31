# Generated by Django 4.1.5 on 2023-04-21 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0009_alter_bedenayakkabi_fiyat_alter_bedenkiyafet_fiyat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000, verbose_name='Yorum')),
                ('date_now', models.DateTimeField(verbose_name='Tarih-Saat')),
                ('star', models.IntegerField(verbose_name='Yorum Puanı')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.urunler', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
