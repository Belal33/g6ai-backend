from rest_framework.authtoken.models import Token
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser

# database_sync_to_async: 
#   It is used for retrieving the data from the database as Django ORM is totally synchronous.
@database_sync_to_async
def returnUser(token_string):
    try:
        user = Token.objects.get(key=token_string).user
    except:
        user = AnonymousUser()
    return user



class TokenAuthMiddleWare:
    def __init__(self, app):
    # In the __init__ function we define the current instance app 
    # to the app which is passed into the stack
        self.app = app

    async def __call__(self, scope, receive, send):
      # . The scope is the dictionary, which functions similarly to the request parameter in function-based views (def fun(request)) 
        query_string = scope["query_string"]
        query_params = query_string.decode()
        # parse_qs: It is used for parsing the query parameters from string to dict.
        query_dict = parse_qs(query_params)
        token = query_dict["token"][0]
        user = await returnUser(token)
        scope["user"] = user
        return await self.app(scope, receive, send)