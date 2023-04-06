from django.db import models
from django.contrib.auth.models import AbstractUser 
import uuid
class CustomUser(AbstractUser):
  temp_id = models.UUIDField(default=uuid.uuid4, unique=True )

  age = models.IntegerField(blank=True,null=True)
