# Generated by Django 4.2.1 on 2023-05-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0011_custompackages_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
