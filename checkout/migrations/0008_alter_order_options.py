# Generated by Django 3.2.13 on 2022-06-08 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_order_courses_bought'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['date']},
        ),
    ]
