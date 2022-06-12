# Generated by Django 3.2.13 on 2022-06-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_examskill_further_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examskill',
            name='exam_name',
            field=models.CharField(choices=[('KET', 'KET'), ('PET', 'PET'), ('FCE', 'FCE'), ('CAE', 'CAE'), ('CPE', 'CPE'), ('IELTS', 'IELTS')], max_length=50),
        ),
        migrations.AlterField(
            model_name='examskill',
            name='exam_section',
            field=models.CharField(blank=True, choices=[('Reading', 'Reading'), ('Writing', 'Writing'), ('Speaking', 'Speaking'), ('Listening', 'Listening')], max_length=20),
        ),
    ]