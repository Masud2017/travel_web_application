# Generated by Django 4.2.1 on 2023-05-28 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0020_histories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'permissions': (('add_orders_for_user', 'add orders for user'), ('change_orders_for_user', 'change orders for user'), ('delete_orders_for_user', 'delete orders for user'), ('view_orders_for_user', 'view orders for user')), 'verbose_name_plural': 'Orders'},
        ),
    ]
