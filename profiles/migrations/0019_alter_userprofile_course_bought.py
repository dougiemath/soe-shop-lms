# Generated by Django 3.2.13 on 2022-06-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_course_course_bought'),
        ('profiles', '0018_auto_20220607_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='course_bought',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]
