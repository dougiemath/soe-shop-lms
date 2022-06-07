# Generated by Django 3.2.13 on 2022-06-03 12:26

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('KET', 'KET'), ('PET', 'PET'), ('FCE', 'FEC'), ('CAE', 'CAE'), ('CPE', 'CPE'), ('IELTS', 'IELTS')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Exam Categories',
            },
        ),
        migrations.CreateModel(
            name='ExamSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(choices=[('KET', 'KET'), ('PET', 'PET'), ('FCE', 'FEC'), ('CAE', 'CAE'), ('CPE', 'CPE'), ('IELTS', 'IELTS')], max_length=50)),
                ('exam_section', models.CharField(blank=True, choices=[('Reading', 'Reading'), ('writing', 'Writing'), ('Speaking', 'Speaking'), ('Listening', 'Listening')], max_length=20)),
                ('question_type', models.CharField(max_length=100)),
                ('question_image', models.ImageField(choices=[('/reading.jpg', 'Reading'), ('/writing.jpg', 'Writing'), ('/listening.jpg', 'Listening'), ('/speaking.jpg', 'Speaking')], default='Reading', upload_to='')),
                ('question_overview', models.TextField()),
                ('sample_question_text', models.TextField()),
                ('sample_question_questions', models.TextField()),
                ('question_approach', models.TextField()),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('upload_questions', models.FileField(blank=True, upload_to='')),
                ('upload_answers', models.FileField(blank=True, upload_to='')),
            ],
            options={
                'ordering': ['exam_name'],
            },
        ),
    ]