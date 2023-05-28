# Generated by Django 4.2.1 on 2023-05-28 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0026_flights_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotels',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='user_model_exnteded',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.usermodelextended'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
