# Generated by Django 5.0.6 on 2024-10-09 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0054_remove_user_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumniprofile',
            name='profile_picture_url',
        ),
        migrations.RemoveField(
            model_name='hodprincipalprofile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='department',
        ),
    ]
