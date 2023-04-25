from rest_framework import serializers
from .models import ChatBox,ChatMessage

class ChatBoxSerializer(serializers.ModelSerializer):
  
  class Meta:
    model=ChatBox
    fields = (
      "id",
      "name",
      "temperature",
      "sys_messages",
      "created_at",
    )


class ChatMessageSerializer(serializers.ModelSerializer):

  chatbox = serializers.PrimaryKeyRelatedField(read_only=True)
  
  def validate_chatbox(self, value):
    request = self.context['request']
    if value.user != request.user:
        raise serializers.ValidationError("Invalid chatbox for that user")
    return value
  
  class Meta:
    model=ChatMessage
    fields = (
      "id",
      "chatbox",
      "user_msg",
      "assistant_msg",
      "n_prompt_messages",
      "finish_reason",
      "voice_message",
      "created_at",
    )

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