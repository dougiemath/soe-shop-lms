# Generated by Django 3.2.13 on 2022-06-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20220616_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='newsletter',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
