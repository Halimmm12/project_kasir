# Generated by Django 4.1.2 on 2022-10-22 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_ketegori_produk_kategori'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ketegori',
            new_name='Kategori',
        ),
    ]
