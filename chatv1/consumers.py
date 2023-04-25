from channels.generic.websocket import JsonWebsocketConsumer
from .chatbot_stream import get_gpt_chat_response
from django.contrib.auth import get_user_model

get_user_model().is_anonymous
get_user_model().is_authenticated

class TokenAuthConsumer(JsonWebsocketConsumer):
  
    def connect(self):
      user = self.scope.get("user")
      if user and user.is_authenticated and not user.is_anonymous:
        self.accept()
      elif user.is_anonymous :
        self.close(code=400)
      else: 
        self.close(code=401)
      

    # def disconnect(self, close_code):
    #     ...

    def receive_json(self, message):
      full_res =''
      # e = get_gpt_chat_response([{"role": "user", "content": "hi"}])
      content = message.get("content")
      print(content)
      for m in get_gpt_chat_response([{"role": "user", "content": content}],"55"):
        print("*"*10)
        print(m["choices"][0]["delta"])
        print(m["choices"][0]["finish_reason"])
        print("*"*10)

        delta = m["choices"][0]["delta"]
        message = delta.get("content")

        if message :      
          full_res += message
          self.send_json({"role": "assistant", "content": message,"finish_reason":m["choices"][0]["finish_reason"]})
        else:
          self.send_json({"role": "", "content": "","finish_reason":m["choices"][0]["finish_reason"]})
      print(full_res)
