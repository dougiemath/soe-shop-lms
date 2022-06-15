# Generated by Django 3.2.13 on 2022-06-15 08:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0033_auto_20220615_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='card_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="What is a brief description of your course?  This will appear in the shop's search results."),
        ),
    ]
