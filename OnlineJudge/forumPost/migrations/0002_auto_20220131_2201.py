# Generated by Django 2.1.7 on 2022-01-31 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumPost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumcomment',
            name='edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]
