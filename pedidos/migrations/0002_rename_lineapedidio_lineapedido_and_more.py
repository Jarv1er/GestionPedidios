# Generated by Django 4.2.2 on 2023-07-28 18:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_rename_prducto_producto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LineaPedidio',
            new_name='LineaPedido',
        ),
        migrations.RenameModel(
            old_name='Pedidio',
            new_name='Pedido',
        ),
    ]
