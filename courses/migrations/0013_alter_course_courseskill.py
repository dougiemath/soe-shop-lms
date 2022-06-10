# Generated by Django 3.2.13 on 2022-06-10 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0013_courseskill_course_num'),
        ('courses', '0012_course_courseskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseskill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.courseskill', verbose_name='EXAM: (Leave blank if your course is General English)'),
        ),
    ]
