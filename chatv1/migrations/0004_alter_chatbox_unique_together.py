# Generated by Django 4.0.10 on 2023-04-26 02:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatv1', '0003_alter_chatmessage_finish_reason'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chatbox',
            unique_together={('user', 'name')},
        ),
    ]
