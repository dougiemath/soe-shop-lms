# Generated by Django 3.2.13 on 2022-06-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_auto_20220608_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examskill',
            name='sample_question_text',
            field=models.TextField(blank=True, verbose_name='Section 2 - Sample Reading Passage'),
        ),
    ]
