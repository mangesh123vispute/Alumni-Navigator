# Generated by Django 5.0.6 on 2024-08-08 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0030_alter_user_college_alter_user_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='admin',
        ),
        migrations.AlterField(
            model_name='alumnipost',
            name='Image',
            field=models.ImageField(blank=True, default='default/def.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='alumnipost',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
