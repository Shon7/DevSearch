# Generated by Django 4.0.4 on 2022-06-01 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='decription',
            new_name='description',
        ),
    ]
