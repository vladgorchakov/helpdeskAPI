# Generated by Django 4.0.6 on 2022-07-28 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='past_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helpdesk.message'),
        ),
    ]