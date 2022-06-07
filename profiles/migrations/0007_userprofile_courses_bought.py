# Generated by Django 3.2.13 on 2022-06-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course'),
        ('profiles', '0006_remove_userprofile_courses_bought'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='courses_bought',
            field=models.ManyToManyField(blank=True, to='courses.Course'),
        ),
    ]