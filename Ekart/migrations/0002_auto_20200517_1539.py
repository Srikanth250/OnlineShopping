# Generated by Django 3.0.6 on 2020-05-17 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ekart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.CharField(max_length=250),
        ),
    ]
