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

class CategoryWithChildSerializer(CategorySerializer):
    childs = serializers.SerializerMethodField()

    def get_childs(self, obj):
        childs_qs = obj.child_cat.all()
        return CategorySerializer(childs_qs, many=True).data