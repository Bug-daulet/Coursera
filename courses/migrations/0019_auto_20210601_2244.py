# Generated by Django 3.0.14 on 2021-06-01 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20210601_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='pozicioni',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='lenda',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='titulli',
            new_name='title',
        ),
    ]