# Generated by Django 4.1.1 on 2023-02-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0028_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]