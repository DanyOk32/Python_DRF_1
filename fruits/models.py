from django.db import models


class NewFruitModel(models.Model):
    class Meta:
        db_table = 'fruits_2_table'
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    weight = models.FloatField()
    status = models.BooleanField(default=False)
