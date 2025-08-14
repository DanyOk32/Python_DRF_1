from django.db import models

class PizzaQuerySet(models.QuerySet):
    def less_than_size(self,size):
        return self.filter(size__lte=size)
    def onli_jelezno(self):
        return self.filter(name__startswith='Jelezno')

class PizzaManager(models.Manager):
    def get_queryset(self):
        return PizzaQuerySet(self.model)
    def less_than_size(self,size):
        return self.get_queryset().less_than_size(size)
    def onli_jelezno(self):
        return self.get_queryset().onli_jelezno()