from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from hificom.models import Category, SpecificationTable, Specification

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


class SpecificationSerializer(ModelSerializer):
    aliases = serializers.SerializerMethodField()
    class Meta:
        model = Specification
        fields = '__all__'

    def get_aliases(self, obj):
        return [ a.alias for a in obj.aliases.all()]

class SpecTableSerializer(ModelSerializer):
    specs = serializers.SerializerMethodField()
    aliases = serializers.SerializerMethodField()
    class Meta:
        model = SpecificationTable
        fields = '__all__'

    def get_specs(self, obj):
        all_specs = obj.specification_set.all()
        return SpecificationSerializer(all_specs, many=True).data
    def get_aliases(self, obj):
        return [ a.alias for a in obj.aliases.all()]

class CategoryDetailSerializer(CategorySerializer):
    childs = serializers.SerializerMethodField()
    tables = serializers.SerializerMethodField()
    
    def get_childs(self, obj):
        childs_qs = obj.child_cat.all()
        return CategorySerializer(childs_qs, many=True).data

    def get_tables(self, obj):
        tables_qs = obj.specificationtable_set.all()
        return SpecTableSerializer(tables_qs, many=True).data