# Generated by Django 5.0.6 on 2024-10-03 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0038_hodprincipalprofile_publications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hodprincipalprofile',
            name='publications',
        ),
        migrations.RemoveField(
            model_name='hodprincipalprofile',
            name='qualifications',
        ),
        migrations.RemoveField(
            model_name='hodprincipalprofile',
            name='responsibilities',
        ),
        migrations.RemoveField(
            model_name='hodprincipalprofile',
            name='years_of_experience',
        ),
    ]
