from django.shortcuts import render
from .chatbot import GPT_simplified
from django.http.response import JsonResponse
from rest_framework.views import Response 
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import AllowAny


@api_view(["POST"])
@permission_classes([AllowAny,])
def chat_view(request):

    print('#'*20)
    print(dir(request))
    print(type(request.data))
    print((request.data))
    print('#'*20)

    user_message = request.data["message"] or ''#insert_user_message_here
    try:
        old_messges =  request.data["old_messges"] or None #insert_user_message_here
        print(old_messges)
    except:
        old_messges = None #insert_user_message_here

    print("#"*50,user_message)
    # user_message = 'hi'#insert_user_message_here
    chat = GPT_simplified()
    response = {"messages":'something wrong happend'}
    
    for i in range(3):
        try:
            response = chat.new_user_message(user_message,old_messges)
        except Exception as e:
            if i == 2:
                raise Exception(e)
            continue
        else:
            # print("error from module")
            break
    return Response(response,status=200)








