#view for connection socket

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from channels.db import database_sync_to_async


class ChatConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name=None
        self.user_name=None

    async def connect(self):
        if not self.scope['user']:
            return await self.close() #закрию конекшн якщо юзер не залогінений
        await self.accept()
        self.room_name = self.scope['url_route']['kwargs']['room']
        #щоб бачити нейм юзера який спілкується, це сихронна яку треба зробити асинх
        self.user_name = await self.get_profile_name()
        #для повідомлень редіс (ченел конфиг)
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        #повідомлення всім що хтось законект
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'sender',
                'message': f'{self.user_name} joined'
            }
        )
        async def sender(self, data):

            await self.send_json(data)

    @database_sync_to_async
    def get_profile_name(self):
        user = self.scope['user']
        return user.profile.name
