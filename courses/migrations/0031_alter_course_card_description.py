# Generated by Django 3.2.13 on 2022-06-13 15:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0030_rename_courseskill_course_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='card_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]