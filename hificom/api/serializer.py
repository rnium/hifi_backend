from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from hificom.models import Category

class CategorySerializer(ModelSerializer):
    parent = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = '__all__'

        extra_kwargs = {
            'get_features_from_child': {'write_only': True}
        }