# Generated by Django 4.2.1 on 2023-05-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0028_remove_packages_activity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='activity_type',
        ),
        migrations.AddField(
            model_name='activities',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='activities',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='activities',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]