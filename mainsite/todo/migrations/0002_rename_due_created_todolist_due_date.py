# Generated by Django 3.2.4 on 2021-07-22 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='due_created',
            new_name='due_date',
        ),
    ]
