# Generated by Django 4.2.1 on 2023-06-02 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0053_alter_ordercustompackages_custom_packages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordercustompackages',
            options={'verbose_name_plural': 'OrderCustomPackage'},
        ),
        migrations.AlterModelOptions(
            name='orderpackages',
            options={'verbose_name_plural': 'OrderPackage'},
        ),
    ]