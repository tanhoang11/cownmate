# Generated by Django 5.0 on 2024-04-24 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_oder',
            new_name='date_order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='oder',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='oder',
            new_name='order',
        ),
    ]
