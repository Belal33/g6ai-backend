from channels.generic.websocket import JsonWebsocketConsumer
from .chatbot_stream import get_gpt_chat_response
from .models import ChatMessage ,ChatBox


class TokenAuthConsumer(JsonWebsocketConsumer):
  
    def connect(self):
      user = self.scope.get("user")
      if user and user.is_authenticated and not user.is_anonymous:
        print("accept")
        self.accept()
      elif user.is_anonymous :
        print("notaccept")
        self.close(code=400)
      else: 
        print("notaccept")
        self.close(code=401)

      

    # def disconnect(self, close_code):
    #     ...

    # def receive_json(self, message):
    #   full_res =''
    #   # e = get_gpt_chat_response([{"role": "user", "content": "hi"}])
    #   content = message.get("content")
    #   print(content)
    #   for m in get_gpt_chat_response([{"role": "user", "content": content}],"55"):

    #     delta = m["choices"][0]["delta"]
    #     message = delta.get("content")

    #     if message :      
    #       full_res += message
    #       self.send_json({"role": "assistant", "content": message,"finish_reason":m["choices"][0]["finish_reason"]})
    #     else:
    #       self.send_json({"role": "", "content": "","finish_reason":m["choices"][0]["finish_reason"]})
    #   print(full_res)


    def receive_json(self, message):
      user = self.scope["user"]
      full_res = ''
      content = message.get("content")
      print(content)
      chat_box = ChatBox.objects.filter(user=user).first()
      chat_message = ChatMessage(
                                  user=user,
                                  chatbox=chat_box,
                                  user_msg=str(content),
                                )
      for m in get_gpt_chat_response([{"role": "user", "content": content}],"55"):
        delta = m["choices"][0]["delta"]
        message = delta.get("content")
        if message:
          full_res += message
          self.send_json({"role": "assistant", "content": message,"finish_reason":m["choices"][0]["finish_reason"]})
        else:
          chat_message.finish_reason = str(m["choices"][0]["finish_reason"])
          self.send_json({"role": "", "content": "","finish_reason":m["choices"][0]["finish_reason"]})
      print(full_res)
      
      chat_message.assistant_msg = full_res
      chat_message.save()
      # Save the chat message to the database
      
