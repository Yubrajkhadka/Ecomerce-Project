# Generated by Django 4.1.1 on 2023-02-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='photos/products'),
        ),
    ]