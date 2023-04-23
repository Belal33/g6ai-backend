from django.db import models
from django.contrib.auth import get_user_model
import uuid

# class Message(models.Model):
#   id = models.UUIDField( default=uuid.uuid4, unique=True ,primary_key=True,editable=False)
#   user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
#   role = models.CharField(max_length=10,choices=(
#       ("user", "user"),
#       ("assistant", "assistant")
#     )
#   )
#   message_data = models.TextField()
#   n_tokens = models.IntegerField(verbose_name="number of tokens",default=0)
#   created_at = models.DateTimeField(editable=False,auto_now_add=True)


  
#   def __str__(self):
#     return str(self.role)+" message "+str(self.id)


# {
#     "initialization_time": self.__initialization_time,
#     "system_messages": [],
#     "messages": [], 
#     "role": [],
#     "n_tokens": [],
#     "n_returned_messages": [],
# }
