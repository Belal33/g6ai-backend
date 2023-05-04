from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from chatv1.models import ChatBox

User = get_user_model()


def create_chatbox(sender, instance, created, **kwargs):
    if created:
        ChatBox.objects.create(user=instance, name=f"ChatBox-{instance.username}")


post_save.connect(create_chatbox, sender=User)
