from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
import os

from core.services.jwt_service import JWTService, ActionToken, ActivateToken, RecoveryToken
from configs.celery import app

from django.contrib.auth import get_user_model
UserModel = get_user_model()

class EmailService:
    @staticmethod
    @app.task #для селери, считает все ф-ии методы которые помочены, и будет думать что это его таски
    def __send_email(to:str, template_name:str, context:dict,subject:str)->None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(
            to=[to],
            from_email=os.environ.get('EMAIL_FROM'),
            subject=subject,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost/activate/{token}'
        #якщо .delay то чітко цей метод для селері
        cls.__send_email.delay(
            to=user.email,
            template_name='register.html',
            context = {'name':user.profile.name, 'url': url},
            subject='Register'
        )
        #відправить нам лист

        # Для відновлення пароля
    @classmethod
    def recovery(cls,user):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'http://localhost/auth/recovery{token}'
        cls.__send_email(
            to=user.email,
            template_name='recovery.html',
            context = {'url': url},
            subject='Recovery'
        )
        #спам в пошту кожні хв нарпиклад
    @staticmethod
    @app.task
    def spam(cls):
        for user in UserModel.objects.all():
            EmailService.__send_email(user.email, 'spam.html', context={}, subject='Spam')
