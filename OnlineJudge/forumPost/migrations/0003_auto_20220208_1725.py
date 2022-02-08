# Generated by Django 2.1.7 on 2022-02-08 17:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forumPost', '0002_auto_20220131_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumcomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forumcomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forumpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]