from apps.pizza.managers import PizzaManager
from core.enums.regex import RegexEnum
from core.models import BaseModel
from django.db import models
from apps.pizza_shops.models import PizzaShopModel
from django.core import validators as V

from core.services.file_services import upload_pizza_photo


class DaysChoices(models.TextChoices):
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'
class PizzaModel(BaseModel):
    class Meta:
        # ordering = (-'id') - сортування по айді в зворотньому по дефолту
        db_table = 'pizza_table'
    name = models.CharField(max_length=120, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)])
    price = models.FloatField()
    size = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(1000)])
    day = models.CharField(max_length=10, choices=DaysChoices.choices)
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')
    # Всі методи і додатковий функціонал
    photo = models.ImageField(upload_to=upload_pizza_photo, blank=True)
    objects = PizzaManager()