# Generated by Django 4.2.1 on 2023-05-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0029_remove_activities_activity_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='packages',
            name='product_id',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]