# Generated by Django 3.2.13 on 2022-06-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0023_auto_20220610_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]