from django.db.models import QuerySet
from django.http import QueryDict

from rest_framework.exceptions import ValidationError

from apps.pizza.models import PizzaModel, DaysChoices
from apps.pizza.serializers import PizzaSerializer
from django_filters import rest_framework as filters

# def filter_pizza(query:QueryDict)->QuerySet:
#     qs = PizzaModel.objects.all().filter()
#     for k,v in query.items():
#         match k:
#             case 'price_gt':
#                 qs = qs.filter(price__gt=v)
#             case 'price_lt':
#                 qs = qs.filter(price__lt=v)
#             case 'price_lte':
#                 qs = qs.filter(price__lte=v)
#             case 'price_gte':
#                 qs = qs.filter(price__gte=v)
#             case "size_gt":
#                 qs = qs.filter(size__gt=v)
#             case 'size_gte':
#                 qs=qs.filter(size__gte=v)
#             case "size_lt":
#                 qs = qs.filter(size__lt=v)
#             case "size_lte":
#                 qs = qs.filter(size__lte=v)
#             case 'name_startwith':
#                 qs = qs.filter(name__istartswith=v)
#             case 'name_endwith':
#                 qs = qs.filter(name__iendswith=v)
#             case 'name_contains':
#                 qs = qs.filter(name__icontains=v)
#             case 'order':
#                 fields = PizzaSerializer.Meta.fields
#                 allowed_fields = (*fields, *[f'-{field}' for field in fields])
#                 if v not in allowed_fields:
#                     raise ValidationError(f'u value not in allowed fields -{v}')
#                 qs = qs.order_by(v)
#
#             case _:
#
#                 raise ValidationError({'detail':f'"{k}" not allowed'})
#     return qs
class PizzaFilter(filters.FilterSet):
    # змінні = квері парамс    fieldn це поле по якому будем фільтр, лукап = те що писали в фільтрах
    lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    starts_with=filters.CharFilter(field_name='name', lookup_expr='startswith')
    ends_with=filters.CharFilter(field_name='name', lookup_expr='endswith')
    contains=filters.CharFilter(field_name='name', lookup_expr='contains')
    range =filters.RangeFilter(field_name='size') # range_min=2&range_max=100 (qparams)
    #входження в числ проміжки
    price_in=filters.BaseInFilter(field_name='price') #price_in=ті прайси які цікавлять
    day = filters.ChoiceFilter('day', choices=DaysChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            #по яким полям
            'price',
            'size',
            'day',
            'id',
            'name',
            'created_at',
            'updated_at',
        )
    ) #order=name|-name   , можна переназвати ('price', 'asd') #order=asd сортує прайси