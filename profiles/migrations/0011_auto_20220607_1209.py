# Generated by Django 3.2.13 on 2022-06-07 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course'),
        ('profiles', '0010_auto_20220607_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='courses_bought',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='courses_bought',
            field=models.ManyToManyField(blank=True, related_name='user', to='courses.Course'),
        ),
    ]