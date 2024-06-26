# Generated by Django 4.2.1 on 2023-06-02 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0049_remove_packages_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='custompackages',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='custompackages',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='custompackages',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='custompackages',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='custompackages',
            name='activities',
            field=models.ManyToManyField(blank=True, null=True, to='auth_app.activities'),
        ),
        migrations.AlterField(
            model_name='custompackages',
            name='flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.flights'),
        ),
        migrations.AlterField(
            model_name='custompackages',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.hotels'),
        ),
    ]
