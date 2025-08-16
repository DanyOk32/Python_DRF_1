from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async

from core.services.jwt_service import JWTService, SocketToken

@database_sync_to_async
def get_user(token:str | None):
    try:
        return JWTService.verify_token(token, SocketToken)
    except (Exception,):
        pass




class AuthSocketMiddleware(BaseMiddleware):
    #переопределяем метод
    async def __call__(self, scope, receive, send):
        # scope - request в звичайному шштп, тут скоуп
        # print(scope) - багато полів одне з них: query_string де є сокет
        # print([item for item in scope['query_string'].decode('utf8').split('&')])
        # отримаємо масив, з token і іншими парамсами
        token = dict(
            [item.split('=') for item in scope['query_string'].decode('utf8').split('&') if item]
        ).get('token', None)
        # масив ключ-значення, ключ значення, умова иф, це якщо там взагалі щось є
        #щоб робити запити, потрібно перероботи з синхронного в асинхронний
        scope['user'] = await get_user(token=token)
        return await super().__call__(scope, receive, send)