# Generated by Django 4.2.1 on 2023-05-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0037_hotels_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
