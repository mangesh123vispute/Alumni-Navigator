# Generated by Django 4.2.6 on 2024-02-17 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0012_remove_alumnipost_alumni_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnipost',
            name='Alumni',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
