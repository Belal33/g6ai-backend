from django.db import models
from django.contrib.auth.models import AbstractUser 

import uuid

class CustomUser(AbstractUser):
  id = models.UUIDField( default=uuid.uuid4, unique=True ,primary_key=True,editable=False)

  age = models.IntegerField(blank=True,null=True)
