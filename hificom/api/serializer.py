from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from hificom.models import Category

class CategorySerializer(ModelSerializer):
    parent_name = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

        extra_kwargs = {
            'get_features_from_child': {'write_only': True}
        }
    
    def get_parent_name(self, obj):
        if p:=obj.parent:
            return p.title

class CategoryWithChildSerializer(CategorySerializer):
    childs = serializers.SerializerMethodField()

    def get_childs(self, obj):
        childs_qs = obj.child_cat.all()
        return CategorySerializer(childs_qs, many=True).data