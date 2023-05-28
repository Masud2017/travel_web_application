# Generated by Django 4.2.1 on 2023-05-28 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0030_packages_price_packages_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custompackages',
            name='activity',
        ),
        migrations.AddField(
            model_name='custompackages',
            name='activities',
            field=models.ManyToManyField(to='auth_app.activities'),
        ),
        migrations.AddField(
            model_name='custompackages',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='custompackages',
            name='product_id',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='custompackages',
            name='user_model_extended',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth_app.usermodelextended'),
        ),
    ]
