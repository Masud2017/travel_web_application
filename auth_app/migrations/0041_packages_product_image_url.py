# Generated by Django 4.2.1 on 2023-06-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0040_packages_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='product_image_url',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]