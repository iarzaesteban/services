# Generated by Django 4.2.9 on 2024-10-07 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='cliente',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='usuario',
            new_name='user',
        ),
    ]
