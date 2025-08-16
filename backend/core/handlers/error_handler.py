#опишемо логіку щоб джанго розумів
# що наші є екепшини, і якщо вони падають то наші помилки,
# нам потрібно щоб спочатку це, а потім хендлер пайтона
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response

# excepton - яка помилка впала, контекст(де впало що, в якій вю)
def error_handler(exc:Exception, context:dict ):
    #побудуємо словник наші кастомін екс
    handlers = {
        "JWTException": _jwt_validation_exception_handler
    }
    response = exception_handler(exc, context)
    # можемо витягнути який саме екс впав
    exc_class = exc.__class__.__name__
    if exc_class in handlers:
        return handlers[exc_class](exc, context)
    return response
def _jwt_validation_exception_handler(exc,context):
    return Response({'detail':'JWT expired or invalid'}, status=status.HTTP_401_UNAUTHORIZED)
