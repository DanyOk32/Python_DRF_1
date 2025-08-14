from django.core.serializers import serialize
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.user.serializers import UserSerializer

UserModel = get_user_model()
class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
class BlockUserView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)
    def patch(self,*args,**kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer=UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #відправка имйла нижче
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import os
#для штмл
class SendEmailView(GenericAPIView):
    permission_classes = (AllowAny,)
    def get(self,*args,**kwargs):
        template = get_template('test_email.html')
        html_content = template.render({'name':'DJANGO'})
        msg = EmailMultiAlternatives('Test Email',
            from_email=os.environ.get('EMAIL_HOST_USER'),
            to=['danyaverchenko@gmail.com']
            )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response({'message':'Email sent successfully!'}, status.HTTP_200_OK)