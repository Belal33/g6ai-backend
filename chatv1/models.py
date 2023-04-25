from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# chatbox:
# 	-id
# 	-user_id
# 	-name
# 	-temperature
# 	-sys_message
# 	-created_at



class ChatBox(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
  user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='chatboxes')
  #  if ModelA has a field like: model_b = ForeignKeyField(ModelB, related_name='model_as'), this would enable you to access the ModelA instances that are related to your ModelB instance by going model_b_instance.model_as.all().
  name = models.CharField(max_length=40)
  temperature = models.DecimalField(
    default=1,
    max_digits=2,
    decimal_places=1,
    validators=[
      MaxValueValidator(1.5,"1.5 is the maximum temperature"),
      MinValueValidator(0.1,"0.1 is the manimum temperature")
    ]
  )
  # https://docs.djangoproject.com/en/4.0/ref/contrib/postgres/fields/#querying-arrayfield

  sys_messages = ArrayField(
    models.TextField(),
    size=5,blank=True
  )
  created_at = models.DateTimeField(auto_now_add=True,editable=False)

  def __str__(self):
    
    return f"{str(self.name)} chatbox[{self.user.get_username()}]"

  class Meta:
    ordering = ['-created_at']

# message:
# 	-id
# 	-user_id
# 	-chatbox_id
# 	-user_msg
# 	-assistant_msg
# 	-n_prompt_messages
# 	-prompt_tokens
# 	-user_msg_tokens
# 	-assistant_msg_tokens 
# 	-finish_reason
# 	-voice_message
#   -created_at
# 	-used_credits


class ChatMessage(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='chatmessages')
  chatbox = models.ForeignKey(ChatBox,on_delete=models.CASCADE,related_name='messages')
  user_msg = models.TextField("user message content")
  assistant_msg = models.TextField("assistant message content")
  n_prompt_messages = models.IntegerField("prompt messages length",default=0)
  prompt_tokens = models.IntegerField("prompt messages tokens",default=0)
  user_msg_tokens = models.IntegerField("user message tokens",default=0)
  assistant_msg_tokens = models.IntegerField("assistant message tokens",default=0)
  finish_reason = models.CharField(max_length=10,null=True,blank=True)
  voice_message = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  used_credits = models.IntegerField(default=0)
  
  def __str__(self):
    return self.user.get_username() + " message | " + str(self.pk)  


  class Meta:
    ordering = ['-created_at']


