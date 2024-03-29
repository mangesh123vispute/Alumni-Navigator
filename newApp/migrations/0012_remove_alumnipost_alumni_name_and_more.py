# Generated by Django 4.2.6 on 2024-02-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0011_alumnipost_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnipost',
            name='alumni_name',
        ),
        migrations.RemoveField(
            model_name='alumnipost',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='alumnipost',
            name='graduation_year',
        ),
        migrations.RemoveField(
            model_name='alumnipost',
            name='public_post',
        ),
        migrations.RemoveField(
            model_name='alumnipost',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='alumnipost',
            name='Image',
            field=models.ImageField(default='default/test.png', upload_to='images'),
        ),
        migrations.AddField(
            model_name='alumnipost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alumnipost',
            name='tag',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='alumnipost',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='alumnipost',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
