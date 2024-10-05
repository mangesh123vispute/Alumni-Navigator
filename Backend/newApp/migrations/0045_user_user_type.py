# Generated by Django 5.0.6 on 2024-10-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0044_remove_alumniprofile_projects_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('alumni', 'Alumni'), ('hod', 'HOD')], default='student', max_length=10),
        ),
    ]
