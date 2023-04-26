from channels.generic.websocket import JsonWebsocketConsumer
from .chatbot_stream import get_gpt_chat_response,prepare_msgs,gpt3_tokens_calc

from channels.db import database_sync_to_async

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
      from .models import ChatMessage ,ChatBox
      
      assistant_msg = ''
      user = self.scope["user"]

      # for testing
      content = [["user",message.get("content")]]
      
      # content = list(message.get("content")) #  [["role","content"],["role","content"],]
      
      new_msg = content[0][1] if content else ""
      
      try:
        chat_box = ChatBox.objects.filter(user=user).first()
        sys_msg = chat_box.sys_message
      except:
        sys_msg = ''
        
      content.append(["system",sys_msg])

      
      prepared_msgs_data = prepare_msgs(content)
      chat_message = ChatMessage(
                                  user=user,
                                  chatbox=chat_box,
                                  user_msg=new_msg,
                                )
      chat_message.n_prompt_messages = int(prepared_msgs_data.get("n_prompt_messages"))
      chat_message.prompt_tokens = int(prepared_msgs_data.get("prompt_tokens"))
      chat_message.user_msg_tokens = gpt3_tokens_calc(new_msg)
      #######################
      # chat_message.used_credits =     
      #######################
      try:
        ######### generator response #########
        for m in get_gpt_chat_response(prepared_msgs_data.get("messages"),str(user.id)):
          delta = m["choices"][0]["delta"]
          message = delta.get("content")
          if message:
            assistant_msg += message
            self.send_json({"role": "assistant", "content": message,"finish_reason":m["choices"][0]["finish_reason"]})
          else:
            chat_message.finish_reason = str(m["choices"][0]["finish_reason"])
            self.send_json({"role": "", "content": "","finish_reason":m["choices"][0]["finish_reason"]})
        print(assistant_msg)
        chat_message.assistant_msg = assistant_msg
        chat_message.assistant_msg_tokens = int(gpt3_tokens_calc(assistant_msg))
        ######### generator response #########
      # if response error
      except:
        chat_message.finish_reason = "openai.error"
        self.send_json({"error": "openai.error"})
        
      chat_message.save()
      
