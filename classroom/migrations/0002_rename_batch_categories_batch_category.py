# Generated by Django 3.2.3 on 2021-06-13 05:41

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='batch_categories',
            new_name='Batch_Category',
        ),
    ]
