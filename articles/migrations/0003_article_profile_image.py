# Generated by Django 4.0.6 on 2022-08-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_article_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]