# Generated by Django 4.1.10 on 2023-08-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollments',
            name='status',
            field=models.CharField(max_length=60),
        ),
    ]
