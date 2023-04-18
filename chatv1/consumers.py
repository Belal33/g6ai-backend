from channels.generic.websocket import JsonWebsocketConsumer
from .chatbot_stream import get_gpt_chat_response

class TokenAuthConsumer(JsonWebsocketConsumer):
  
    def connect(self):
      self.accept()
      print(self.scope["user"].username)
      

    def disconnect(self, close_code):
        ...

    def receive_json(self, message):
      full_res =''
      # e = get_gpt_chat_response([{"role": "user", "content": "hi"}])
      content = message.get("content")
      print(content)
      for m in get_gpt_chat_response([{"role": "user", "content": content}]):
        

        delta = m["choices"][0]["delta"]
        message = delta.get("content",None)

        if message :      
          full_res += message
          self.send_json({"role": "assistant", "content": message})
      print(full_res)
