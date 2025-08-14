from rest_framework import serializers

from apps.pizza.models import PizzaModel


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields =('id','name','price','size','day', 'created_at','updated_at')
    def validate_price(self,price):
        if price <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return price
    def validate(self, attrs):
        price = attrs.get('price')
        size = attrs.get('size')
        if price == size:
            raise serializers.ValidationError('Size cant be eq to price')
        return attrs
class PizzaPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaModel
        fields =('photo',)

    # name = serializers.CharField(max_length=120)
    # price = serializers.FloatField()вщслук
    # size = serializers.IntegerField()
    # id = serializers.IntegerField(read_only=True)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
    # def create(self, validated_data):
    #     return PizzaModel.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #         instance.save()
    #     return instance