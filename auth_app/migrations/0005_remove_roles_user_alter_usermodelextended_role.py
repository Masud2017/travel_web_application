# Generated by Django 4.2.1 on 2023-05-21 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_usermodelextended_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roles',
            name='user',
        ),
        migrations.AlterField(
            model_name='usermodelextended',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.roles'),
        ),
    ]
