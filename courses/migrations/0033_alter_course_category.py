# Generated by Django 3.2.13 on 2022-06-22 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0032_auto_20220621_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.category', verbose_name='What is category of your lesson? It can beGeneral English or Exam Skills.'),
        ),
    ]
