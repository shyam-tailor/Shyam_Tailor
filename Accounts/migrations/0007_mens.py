# Generated by Django 3.0.6 on 2020-07-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_auto_20200712_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(default='', max_length=500)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default='')),
                ('pub_date', models.DateField(default='')),
                ('image', models.ImageField(default='', upload_to='static/images')),
                ('detailimage', models.ImageField(default='', upload_to='static/images')),
                ('detailimage2', models.ImageField(default='', upload_to='static/images')),
                ('detailimage3', models.ImageField(default='', upload_to='static/images')),
                ('detailimage4', models.ImageField(default='', upload_to='static/images')),
            ],
        ),
    ]
