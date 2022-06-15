# Generated by Django 3.2.13 on 2022-06-15 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0028_alter_lessons_further_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lms.lessoncategory', verbose_name='Choose a category for this lesson.  If it is a new category, not in the list, you will need to create a category in the previous section first.'),
        ),
    ]
