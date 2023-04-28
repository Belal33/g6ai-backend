import openai
import tiktoken
from environs import Env # new

env = Env() # new
env.read_env() # new

openai.api_key=env.str("OPENAI_APIKEY")




def gpt3_tokens_calc(argument, chat=False, encoding=tiktoken.get_encoding("cl100k_base")):
    # sourcery skip: remove-redundant-if
    if chat:
        num_tokens = 0
        for message in argument:
            # every message follows <im_start>{role/name}\n{content}<im_end>\n
            num_tokens += 4
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens + 1
    elif not chat:
        encoded_string = encoding.encode(argument)
        tokens = [encoding.decode([token]) for token in encoded_string]
        return len(tokens)


def prepare_msgs(msgs:list[list[str]]):  # sourcery skip: merge-nested-ifs, switch
    """
    returned data
    {
        "messages": messages,
        "prompt_tokens": prompt_tokens,
        "n_prompt_messages": n_prompt_messages,
    }
    """
    max_prompt_tokens = 500
    prompt_tokens = 0
    chat_msg_returned = False
    messages = []
    for role, msg in msgs:
        if role == "system":
            # if gpt3_tokens_calc(msg) > 100:
            #     raise Exception(
            #         f"system messages can't contain more than 100 tokens\ncurrent message contain {gpt3_tokens_calc(msg)} tokens")
            messages.append({"role": role, "content": msg})
    q = len(messages)
    for role, msg in msgs:
        if role == "system":
            continue
        if role == "assistant" and not chat_msg_returned:
            messages.insert(q, {"role": role, "content": msg})
            chat_msg_returned = True
        if role == "user":
            messages.insert(q, {"role": role, "content": msg})
        prompt_tokens = gpt3_tokens_calc(messages, chat=True)
        if prompt_tokens >= max_prompt_tokens:
            break

    n_prompt_messages = len(messages)

    data = {
        "messages": messages,
        "prompt_tokens": prompt_tokens,
        "n_prompt_messages": n_prompt_messages,
    }
    return data


def get_gpt_chat_response(
        messages,
        user_id,
        model="gpt-3.5-turbo",
        temperature=1,
        max_tokens=1000
    ):  # sourcery skip: inline-immediately-returned-variable, raise-from-previous-error, remove-unreachable-code
    for i in range(5):
        try:
            res = openai.ChatCompletion.create(model=model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stream=True,
                    user=user_id,
                )
            return res
        except (openai.error.TryAgain,
                openai.error.ServiceUnavailableError,
                openai.error.APIError,
                openai.error.APIConnectionError,
                openai.error.Timeout
                ) as err:
            if i == 4:
                raise Exception(err)
            continue


def transcripe(path):
    audio_file = open(path, "rb")
    res = openai.Audio.transcribe("whisper-1", audio_file)
    return res.text



# msg = prepare_msgs([
#     ("system", "1"),
#     ("system", "2"),
#     ("user", "8  "),
#     ("assistant", "7"),
#     ("user", "6"),
#     ("assistant", "5"),
#     ("user", "4"),
#     ("assistant", "3")
# ])

# for i in get_gpt_chat_response(msg, "0"):
#     print(i.choices[0].delta)

# print(msg)

# e = get_gpt_chat_response([{"role": "user", "content": "hi"}])
