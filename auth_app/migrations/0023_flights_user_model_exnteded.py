# Generated by Django 4.2.1 on 2023-05-28 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0022_alter_cancellations_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='user_model_exnteded',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.usermodelextended'),
        ),
    ]
