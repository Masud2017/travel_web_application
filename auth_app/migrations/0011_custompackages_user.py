# Generated by Django 4.2.1 on 2023-05-25 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0010_remove_orders_activity_remove_orders_flight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='custompackages',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth_app.usermodelextended'),
        ),
    ]
