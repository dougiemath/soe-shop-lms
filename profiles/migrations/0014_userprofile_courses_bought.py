# Generated by Django 3.2.13 on 2022-06-07 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_course_courses_bought'),
        ('profiles', '0013_remove_userprofile_courses_bought'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='courses_bought',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course'),
        ),
    ]