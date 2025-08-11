from core.models import BaseModel
from django.db import models

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizza_table1'
    name = models.CharField(max_length=100)
    size= models.IntegerField()
    price = models.FloatField()
