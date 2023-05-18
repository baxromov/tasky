from django_filters import FilterSet
from django_filters import rest_framework as filters

from task_3 import models


class ProductFilterSet(FilterSet, filters.OrderingFilter):
    ordering = filters.OrderingFilter(fields=[
        'id',
        'name',
        'price',
        'description',
    ])

    class Meta:
        model = models.Product
        fields = [
            'status',
        ]
