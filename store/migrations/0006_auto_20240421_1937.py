# Generated by Django 5.0.4 on 2024-04-21 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer_store_custo_first_n_a7e990_idx'),
    ]

    operations = [
        migrations.RunSQL(
            '''INSERT INTO store_collection (title)
            VALUES ("COLLECTION1")''', 
            
            '''DELETE FROM store_collection 
            WHERE title="COLLECTION1"
            '''
        )
    ]