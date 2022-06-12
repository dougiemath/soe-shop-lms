# Generated by Django 3.2.13 on 2022-06-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0017_alter_coursecategory_name'),
        ('courses', '0015_auto_20220610_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='courseskill',
        ),
        migrations.AddField(
            model_name='course',
            name='courseskill',
            field=models.ManyToManyField(blank=True, null=True, to='lms.CourseSkill', verbose_name='EXAM: (Leave blank if your course is General English)'),
        ),
    ]