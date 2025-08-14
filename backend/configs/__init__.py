from .celery import app as celery_app

__all__ = ['celery_app']

# коли буде звертатись по пакету конфігурацій, він одразу зможе забрати звідси селері ап