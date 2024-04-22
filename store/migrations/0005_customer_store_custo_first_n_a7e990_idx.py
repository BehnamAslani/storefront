# Generated by Django 5.0.4 on 2024-04-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_table'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['first_name', 'last_name'], name='store_custo_first_n_a7e990_idx'),
        ),
    ]