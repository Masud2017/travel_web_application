# Generated by Django 4.2.1 on 2023-06-02 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0056_remove_ordercustompackages_custom_packages_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cancellations',
        ),
    ]
