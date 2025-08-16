from rest_framework import serializers
from django.contrib.auth import get_user_model
UserModel = get_user_model()

class EmailSerializer(serializers.Serializer):
    #Modul Serializer не можна, бо він буде перевіряти на унікальність імейла
    email = serializers.EmailField()

    #валідація пароля при сбросі через імейл
class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['password']