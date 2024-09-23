# Generated by Django 5.0.1 on 2024-03-25 17:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0021_user_followers_remove_user_following_user_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0, null=True), size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0, null=True), size=None),
        ),
    ]