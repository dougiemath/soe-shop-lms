# Generated by Django 3.2.13 on 2022-06-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_course_courses_bought'),
        ('profiles', '0014_userprofile_courses_bought'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='courses_bought',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='courses_bought',
            field=models.ManyToManyField(blank=True, to='courses.Course'),
        ),
    ]