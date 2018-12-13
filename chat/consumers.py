import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


from .models import Thread,ChatMessage
class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connected",event)
        await self.send({
        "type":"websocket.accept"
        })
        other_user=self.scope['url_route']['kwargs']['username']
        me=self.scope['user']
        print(other_user,me)
        thread_obj=await self.get_thread(me,other_user)
        print(thread_obj)

    async def websocket_recieve(self,event):
        # when a message is recieved
        print("recieved",event)

    async def websocket_disconnect(self,event):
        #when the websocket disconnects
        print("disconnect",event)

    @database_sync_to_async
    def get_thread(self,user,other_username):
        return Thread.objects.get_or_new(user,other_username)[0]
