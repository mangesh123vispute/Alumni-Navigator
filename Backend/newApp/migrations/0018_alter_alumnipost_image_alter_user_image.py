# Generated by Django 4.2.6 on 2024-02-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0017_alter_user_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnipost',
            name='Image',
            field=models.ImageField(default='default/def.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Image',
            field=models.ImageField(default='default/def.jpeg', upload_to='images'),
        ),
    ]
