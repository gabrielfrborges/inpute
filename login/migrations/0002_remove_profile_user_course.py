# Generated by Django 2.2.5 on 2019-09-19 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_course',
        ),
    ]
