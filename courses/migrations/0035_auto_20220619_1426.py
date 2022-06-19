# Generated by Django 3.2.13 on 2022-06-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0034_alter_course_card_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='card_description',
            field=models.TextField(blank=True, null=True, verbose_name="What is a brief description of your course?  This will appear in the shop's search results."),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name="What is a detailed description of your course?  This will appear on the course's dedicated page, so be as detailed as you like."),
        ),
    ]