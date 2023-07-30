# Generated by Django 3.2.20 on 2023-07-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_alter_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_cat',
        ),
        migrations.AddField(
            model_name='product',
            name='fixed_price',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='negotiable_price',
            field=models.BooleanField(default=False),
        ),
    ]