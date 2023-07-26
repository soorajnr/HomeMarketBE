# Generated by Django 3.2.20 on 2023-07-26 06:46

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=300)),
                ('photo', models.ImageField(blank=True, upload_to='images')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('quantity', models.FloatField(blank=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('price_cat', models.CharField(blank=True, max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.category_class')),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userapp.user')),
            ],
        ),
    ]
