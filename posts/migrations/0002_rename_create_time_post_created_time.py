# Generated by Django 4.2.3 on 2023-07-12 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_time',
            new_name='created_time',
        ),
    ]