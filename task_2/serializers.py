from rest_framework import serializers
from task_2.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'parent', 'children')
        read_only_fields = ('id', 'children')

    def get_children(self, obj):
        children = Category.objects.filter(parent=obj)
        serializer = CategorySerializer(children, many=True, context=self.context)
        return serializer.data

    def validate_name(self, value):
        # Perform field-specific validation on the 'name' field
        # For example, check if the name is unique within its parent category
        parent = self.context.get('parent')
        if parent and Category.objects.filter(parent=parent, name=value).exists():
            raise serializers.ValidationError("Category with this name already exists within the parent category.")
        return value

    def to_representation(self, instance):
        # Perform data transformation for specific fields before serialization
        representation = super().to_representation(instance)
        representation['name'] = representation['name'].upper()
        return representation
