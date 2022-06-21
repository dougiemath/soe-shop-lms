# Generated by Django 3.2.13 on 2022-06-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_contact_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='newsletter',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Would you like to sign up for our newsletter?'),
        ),
    ]
