from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import BlacklistMixin, Token
from typing import Type

from core.enums.action_token_enum import ActionTokenEnum
from core.exceptions.jwt_exception import JWTException
from rest_framework.generics import get_object_or_404

UserModel = get_user_model()
ActionTokenClassType = Type[BlacklistMixin|Token]

class ActionToken(BlacklistMixin, Token):
    pass
#клас токену
class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime

#відновлення токену
class RecoveryToken(ActionToken):
    token_type = ActionTokenEnum.RECOVERY.token_type
    lifetime = ActionTokenEnum.RECOVERY.lifetime

class JWTService:
    # 2-верифікує, 1-створювати
    @staticmethod
    def create_token(user,token_class:ActionTokenClassType):
        return token_class.for_user(user)
    #перевірка
    @staticmethod
    def verify_token(token,token_class:ActionTokenClassType):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except Exception:
            raise JWTException
        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)

#для сокетів!
class SocketToken(ActionToken):
    token_type = ActionTokenEnum.SOCKET.token_type
    lifetime = ActionTokenEnum.SOCKET.lifetime