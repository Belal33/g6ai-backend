from django.db import models
from django.contrib.auth.models import AbstractUser 
import uuid
class CustomUser(AbstractUser):
  user_id = models.UUIDField(max_length=36, default=uuid.uuid4, unique=True ,editable=False)

  age = models.IntegerField(blank=True,null=True)
