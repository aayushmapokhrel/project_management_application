# Generated by Django 4.2.17 on 2024-12-28 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_delete_comment'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
