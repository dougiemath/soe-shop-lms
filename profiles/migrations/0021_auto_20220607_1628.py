# Generated by Django 3.2.13 on 2022-06-07 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_course_course_bought'),
        ('profiles', '0020_alter_userprofile_course_bought'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='course_bought',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='course_brought',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]