# Generated by Django 4.2.1 on 2023-05-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0033_remove_custompackages_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
