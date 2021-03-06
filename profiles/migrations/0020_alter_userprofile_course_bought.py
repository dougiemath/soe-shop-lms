# Generated by Django 3.2.13 on 2022-06-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_course_course_bought'),
        ('profiles', '0019_alter_userprofile_course_bought'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='course_bought',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Course'),
        ),
    ]
