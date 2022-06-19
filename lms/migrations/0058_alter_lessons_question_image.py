# Generated by Django 3.2.13 on 2022-06-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0057_alter_lessons_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='question_image',
            field=models.CharField(choices=[('https://res.cloudinary.com/corderoybear/image/upload/v1655371458/static/media/reading.9b0786861128.jpg', 'Reading'), ('https://res.cloudinary.com/corderoybear/image/upload/v1655371458/static/media/writing.23e6ff8e3f48.jpg', 'Writing'), ('https://res.cloudinary.com/corderoybear/image/upload/v1655371457/static/media/listening.a10f4492e111.jpg', 'Listening'), ('https://res.cloudinary.com/corderoybear/image/upload/v1655371459/static/media/speaking.8e29b8f0faba.jpg', 'Speaking')], default='Reading', max_length=200, verbose_name='What skill does the lesson relate to?'),
        ),
    ]
