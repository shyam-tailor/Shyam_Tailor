# Generated by Django 3.0.6 on 2020-06-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeapp', '0002_auto_20200623_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]