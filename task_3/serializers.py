from rest_framework import serializers

from task_3 import models


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
