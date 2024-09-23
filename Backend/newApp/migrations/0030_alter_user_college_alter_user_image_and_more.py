# Generated by Django 5.0.1 on 2024-05-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0029_rename_alumni_alumnipost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='College',
            field=models.CharField(blank=True, choices=[('SSBT COET, Jalgaon', 'SSBT COET, Jalgaon')], default='SSBT COET', max_length=80),
        ),
        migrations.AlterField(
            model_name='user',
            name='Image',
            field=models.ImageField(blank=True, default='default/def.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.TextField(blank=True, default='[]'),
        ),
        migrations.AlterField(
            model_name='user',
            name='linkedin',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]