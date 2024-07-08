from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from hificom.models import Category, SpecificationTable, Specification, Product, ProductImage

class CategoryBasicSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


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
    category_tree = serializers.SerializerMethodField()
    tree_tables = serializers.SerializerMethodField()
    
    def get_childs(self, obj):
        childs_qs = obj.child_cat.all()
        return CategorySerializer(childs_qs, many=True).data

    def get_tables(self, obj):
        tables_qs = obj.specificationtable_set.all()
        return SpecTableSerializer(tables_qs, many=True).data
    
    def get_category_tree(self, obj):
        return CategoryBasicSerializer(obj.category_tree, many=True).data
    
    def get_tree_tables(self, obj):
        tables = SpecificationTable.objects.filter(category__in=obj.category_tree)
        return SpecTableSerializer(tables, many=True).data


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['main']


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(ModelSerializer):
    images = serializers.ListField(
        child = serializers.ImageField(),
        required = False
    )
    tables = serializers.ListField()
    class Meta:
        model = Product
        exclude = ['tags', 'slug']
    
    def create(self, validated_data):
        images = validated_data.pop('images')
        tables = validated_data.pop('tables')
        print(tables, flush=1)
        return super().create(validated_data)