# Generated by Django 3.2.3 on 2021-06-15 16:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidcourse',
            name='desciption',
            field=ckeditor.fields.RichTextField(blank=True, default='open', null=True),
        ),
    ]
