# Generated by Django 4.0.6 on 2022-08-03 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='profile_image',
        ),
    ]