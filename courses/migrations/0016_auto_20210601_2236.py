# Generated by Django 3.0.14 on 2021-06-01 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20210601_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klasa',
            old_name='pershkrimi',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='klasa',
            old_name='imazhi',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='klasa',
            old_name='titulli',
            new_name='title',
        ),
    ]
