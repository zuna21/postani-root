# Generated by Django 4.0.6 on 2022-08-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profiles'),
        ),
    ]
