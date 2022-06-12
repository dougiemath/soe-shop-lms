# Generated by Django 3.2.13 on 2022-06-12 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0029_alter_course_category'),
        ('lms', '0025_rename_courseskill_lessons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseCategory',
            new_name='LessonCategory',
        ),
        migrations.AlterModelOptions(
            name='lessoncategory',
            options={'verbose_name_plural': 'Lesson Categories'},
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'ordering': ['name'], 'verbose_name_plural': 'Lessons'},
        ),
    ]
