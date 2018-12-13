import aynscio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Thread,ChatMessage

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connected",event)

    async def websocket_recieve(self,event):
        # when a message is recieved
        print("recieved",event)

    async def websocket_disconnect(self,event):
        #when the websocket disconnects
        print("disconnect",event)
