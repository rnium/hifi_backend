from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from hificom.models import (Category, CategoryGroup, SpecificationTable, ProductSpec, 
                            Specification, Product, ProductImage, KeyFeature, Carousel, 
                            ProductCollection, Cart, Coupon, Order)
from . import utils
from django.shortcuts import get_object_or_404


class CategoryBasicSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title', 'short_title']


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


class CategoryGroupSerializer(ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = CategoryGroup
        fields = ['title', 'categories']

    def get_categories(self, obj):
        categories = obj.categories.all()
        return CategoryBasicSerializer(categories, many=True).data


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


class ProductSpecSerializer(ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = ProductSpec
        fields = ['id', 'title', 'value', 'specification']

    def get_title(self, obj):
        return obj.specification.title


class CategoryDetailSerializer(CategorySerializer):
    childs = serializers.SerializerMethodField()
    tables = serializers.SerializerMethodField()
    category_tree = serializers.SerializerMethodField()
    tree_tables = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()
    
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
    
    def get_groups(self, obj):
        cat_groups = CategoryGroup.objects.filter(root__in=obj.category_tree)
        return CategoryGroupSerializer(cat_groups, many=True).data
    

class KeyFeatureSerializer(ModelSerializer):
    feature = serializers.SerializerMethodField()
    class Meta:
        model = KeyFeature
        fields = '__all__'
    
    def get_feature(self, obj):
        return obj.feature


class ProductBasicSerializer(ModelSerializer):
    priceSale = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id', 
            'title',
            'slug',
            'price',
            'priceSale',
            'discount',
            'in_stock',
            'cover',
        ]
    
    def get_priceSale(self, obj):
        if dis:=obj.discount:
            return obj.price - dis
        
    def get_cover(self, obj):
        if cover_img:=obj.productimage_set.first():
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(cover_img.main.url)
            else:
                return cover_img.main.url


class ProductSemiDetailSerializer(ProductBasicSerializer):
    key_features = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_key_features(self, obj):
        return [kf.feature for kf in obj.keyfeature_set.all()]
    

class ProductDetailSerializer(ProductSemiDetailSerializer):
    images = serializers.SerializerMethodField()
    spec_tables = serializers.SerializerMethodField()
    num_ratings = serializers.SerializerMethodField()
    category_tree = serializers.SerializerMethodField()

    def get_images(self, obj):
        images = obj.productimage_set.all()
        request = self.context.get('request')
        if request:
            return [{'id': img.id, 'url': request.build_absolute_uri(img.main.url)} for img in images]
        else:
            return [{'id': img.id, 'url': img.main.url} for img in images]
    
    def get_spec_tables(self, obj):
        product_specs = obj.productspec_set.all()
        table_ids = product_specs.values_list('specification__table', flat=True).distinct()
        tables = SpecificationTable.objects.filter(id__in=table_ids)
        data = []
        for table in tables:
            table_specs = product_specs.filter(specification__table=table)
            table_data = {
                'title': table.title,
                'id': table.id,
                'specs': ProductSpecSerializer(table_specs, many=True).data
            }
            data.append(table_data)
        return data

    def get_num_ratings(self, obj):
        return obj.review_set.all().count()
    
    def get_category_tree(self, obj):
        return CategoryBasicSerializer(obj.category.category_tree, many=True).data


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductCreateSerializer(ModelSerializer):
    images = serializers.ListField(
        child = serializers.ImageField(),
        required = False
    )
    tables = serializers.ListField()
    key_features = serializers.ListField()
    class Meta:
        model = Product
        exclude = ['slug']
    
    def create(self, validated_data):
        images = validated_data.pop('images')
        tables = validated_data.pop('tables')
        key_features = validated_data.pop('key_features')
        product = super().create(validated_data)
        utils.update_product_specs(product, tables)
        img_list = [{'product': product.id, 'main': img} for img in images]
        image_serializer = ProductImageSerializer(data=img_list, many=True)
        if image_serializer.is_valid():
            image_serializer.save()
        else:
            print(image_serializer.errors, flush=1)
        kf_list = [{**kf, 'product': product.id} for kf in key_features]
        kf_serializer = KeyFeatureSerializer(data=kf_list, many=True)
        if kf_serializer.is_valid():
            kf_serializer.save()
        else:
            print(kf_serializer.errors, flush=1)
        return product


class CarouselSerializer(ModelSerializer):
    banner = serializers.SerializerMethodField()
    class Meta:
        model = Carousel
        fields = '__all__'
    
    def get_banner(self, obj):
        if req:=self.context.get('request'):
            return req.build_absolute_uri(obj.banner.url)
        return obj.banner.url


class ProductCollectionSerializer(ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = ProductCollection
        exclude = ['priority']

    def get_products(self, obj):
        return ProductBasicSerializer(
            obj.products.all(), 
            many=True,
            context=self.context
        ).data


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'