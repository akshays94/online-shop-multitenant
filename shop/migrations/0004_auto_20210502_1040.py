# Generated by Django 3.0.7 on 2021-05-02 10:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210502_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
