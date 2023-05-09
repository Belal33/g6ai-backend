from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    age = models.IntegerField(blank=True, null=True)
    user_credits = models.IntegerField(default=0)


@receiver(post_save, sender=CustomUser)
def create_chat_for_new_user(sender, instance, created, **kwargs):
    if created:
        from chatv1.models import ChatBox

        ChatBox.objects.create(user=instance, name="ChatG6")
