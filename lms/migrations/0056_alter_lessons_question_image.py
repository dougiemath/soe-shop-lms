# Generated by Django 3.2.13 on 2022-06-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0055_alter_lessons_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='question_image',
            field=models.CharField(choices=[('1', 'Reading'), ('2', 'Writing'), ('3', 'Listening'), ('4', 'Speaking')], default='Reading', max_length=200, verbose_name='What skill does the lesson relate to?'),
        ),
    ]
