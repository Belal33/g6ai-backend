from channels.generic.websocket import JsonWebsocketConsumer
from .chatbot_stream import get_gpt_chat_response

class TokenAuthConsumer(JsonWebsocketConsumer):
  
    def connect(self):
      self.accept()
      print(self.scope["user"].username)
      
      print(self.scope["user"])
      # print(self.scope["user"].email)

    def disconnect(self, close_code):
        ...

    def receive_json(self, message):
      full_res =''
      # e = get_gpt_chat_response([{"role": "user", "content": "hi"}])
      content = message.get("content")
      print(content)
      for m in get_gpt_chat_response([{"role": "user", "content": content}]):
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
      self.close()
