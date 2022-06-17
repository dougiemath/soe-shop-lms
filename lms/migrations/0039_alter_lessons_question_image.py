# Generated by Django 3.2.13 on 2022-06-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0038_alter_lessons_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='question_image',
            field=models.ImageField(choices=[('reading.jpg', 'Reading'), ('writing.jpg', 'Writing'), ('listening.jpg', 'Listening'), ('speaking.jpg', 'Speaking')], default='Reading', upload_to='', verbose_name='What skill does the lesson relate to?'),
        ),
    ]
