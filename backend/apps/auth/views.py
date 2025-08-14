from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.user.serializers import UserSerializer
from core.services.email_service import EmailService
from core.services.jwt_service import JWTService, ActivateToken, RecoveryToken, SocketToken
from rest_framework import status

from django.contrib.auth import get_user_model

UserModel = get_user_model()
class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)
    def patch (self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Для відновлення
class RecoveryRequestView(GenericAPIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        data =self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=serializer.data['email'])
        EmailService.recovery(user)
        return Response({'details':'link send to email'},status=status.HTTP_200_OK)
#для створення нового паролю, після відправки токену
class RecoveryPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)
    def post(self,*args,**kwargs):
        data = self.request.data
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # перевіряємо пароль, щоб був валідним, перед запитом в бд

        token = kwargs['token']
        #перевірка токена
        user = JWTService.verify_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Для сокетів, щоб приєднувалась лише залогінена людина
class SocketTokenView(GenericAPIView):
    def get(self, *args,**kwargs):
        # новий токен для залогіненого юзера
        token = JWTService.create_token(user=self.request.user, token_class=SocketToken)
        return Response({'token':str(token)}, status.HTTP_200_OK)



#Для відхоплення токену, з надісланого листа. Потім юзер переходить на ФронтеНд, та ми повинні
# відхопити ключ

