from channels.generic.websocket import JsonWebsocketConsumer
from .chatbot_stream import get_gpt_chat_response, prepare_msgs, gpt3_tokens_calc


class TokenAuthConsumer(JsonWebsocketConsumer):
    def connect(self):
        user = self.scope.get("user")

        if user and user.is_authenticated and not user.is_anonymous:
            self.accept()

        elif user.is_anonymous:
            self.close(code=401)

        else:
            self.close(code=401)

    def receive_json(self, res):
        from .models import ChatMessage, ChatBox

        user = self.scope["user"]

        # for testing
        # msgs = [["user", res.get("content")]]
        # chat_id = "344f04fb-589a-4fe2-b2fd-df00da482b26"

        try:
            msgs = list(res.get("content"))  #  [["role","content"],["role","content"],]
            chat_id = res.get("chat_id")

            new_msg = msgs[0][1] if msgs else ""
            new_msg_tokens = gpt3_tokens_calc(new_msg)
        except:
            self.send_json({"error": "this content is not valid"})
            self.close(code=400)

        if not (new_msg_tokens > 399):
            chat_boxes = ChatBox.objects.filter(
                id=chat_id,
                user=user,
            )

            if chat_boxes.count() == 1:
                chat_box = chat_boxes.first()
                sys_msg = chat_box.sys_message
                if sys_msg:
                    print(sys_msg)
                    msgs.append(["system", sys_msg])
                print("no", sys_msg)

            else:
                self.send_json({"error": "this chatbox does not exist"})
                self.close()

            prepared_msgs_data = prepare_msgs(msgs)

            chat_message = ChatMessage(
                user=user,
                chatbox=chat_box,
                user_msg=new_msg,
            )
            chat_message.n_prompt_messages = int(
                prepared_msgs_data.get("n_prompt_messages")
            )
            chat_message.prompt_tokens = int(prepared_msgs_data.get("prompt_tokens"))
            chat_message.user_msg_tokens = gpt3_tokens_calc(new_msg)
            #######################
            # chat_message.used_credits =
            #######################
            try:
                ######### generator response #########
                assistant_msg = ""
                for m in get_gpt_chat_response(
                    prepared_msgs_data.get("messages"), str(user.id)
                ):
                    delta = m["choices"][0]["delta"]
                    message = delta.get("content")

                    status = m["choices"][0]["finish_reason"]

                    if message:
                        assistant_msg += message
                        self.send_json({"content": message, "status": status})
                    else:
                        chat_message.finish_reason = status
                        self.send_json({"content": "", "status": status or "start"})

                chat_message.assistant_msg = assistant_msg
                chat_message.assistant_msg_tokens = int(gpt3_tokens_calc(assistant_msg))
                ######### generator response #########
            # if response error
            except Exception as e:
                chat_message.finish_reason = "openai.error"
                self.send_json({"error": "openai.error", "content": str(e)})
                chat_message.used_credits = 0

            chat_message.save()

        else:
            self.send_json(
                {
                    "content": f"system messages can't contain more than 400 tokens \ncurrent message contain {new_msg_tokens} tokens",
                    "status": "not_valid",
                }
            )
