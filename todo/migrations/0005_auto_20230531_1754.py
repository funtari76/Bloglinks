# Generated by Django 3.2.15 on 2023-05-31 17:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0004_bloglinks_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloglinks',
            name='likes',
        ),
        migrations.AddField(
            model_name='bloglinks',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
