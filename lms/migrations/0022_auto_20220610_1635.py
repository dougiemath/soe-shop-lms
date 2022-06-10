# Generated by Django 3.2.13 on 2022-06-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0021_alter_courseskill_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseskill',
            name='category',
        ),
        migrations.AddField(
            model_name='courseskill',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='lms.CourseCategory'),
        ),
    ]
