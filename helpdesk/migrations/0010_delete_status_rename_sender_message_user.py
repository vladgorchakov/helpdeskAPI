# Generated by Django 4.0.6 on 2022-08-22 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0009_remove_message_past_message_alter_message_ticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='user',
        ),
    ]
