# Generated by Django 5.0.6 on 2024-08-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0032_alter_user_about_alter_user_branch_alter_user_work_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='', max_length=150, unique=True),
        ),
    ]
