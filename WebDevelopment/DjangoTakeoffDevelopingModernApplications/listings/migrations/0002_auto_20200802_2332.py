# Generated by Django 3.0.8 on 2020-08-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='product_type',
            field=models.CharField(choices=[('Bike', 'Bike'), ('Parts', 'Parts'), ('Models', 'Models'), ('Other', 'Other')], default='Bike', max_length=50),
        ),
        migrations.AlterField(
            model_name='listings',
            name='sale_type',
            field=models.CharField(choices=[('Available for pickup', 'Pick Up'), ('Available for shipping', 'Ship')], default='Available for shipping', max_length=50),
        ),
    ]
