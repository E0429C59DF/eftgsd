# Generated by Django 4.1.7 on 2023-04-04 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='beiträge',
            new_name='beitrag',
        ),
    ]
