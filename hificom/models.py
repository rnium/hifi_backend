from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Carousel(models.Model):
    banner = models.ImageField(upload_to='features')
    link = models.URLField()
    added_at = models.DateTimeField(default=timezone.now)


class Category(models.Model):
    category_types = (
        ('general', 'General Category'),
        ('brand', 'Brand Category'),
        ('feature', 'Feature Category'),
        ('tag', 'Tag Under Feature'),
    )
    display_child_types = (
        ('all', 'All Categories'),
        ('none', 'Display No Childs'),
        *category_types
    )
    title = models.CharField(max_length=100)
    cat_type = models.CharField(max_length=20, default='general', choices=category_types)
    slug = models.SlugField(max_length=200, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='parent_cat')
    minprice = models.FloatField(default=0)
    maxprice = models.FloatField(default=0)
    logo = models.ImageField(upload_to='category', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    display_childs = models.CharField(max_length=20, default='brand', choices=display_child_types)
    get_features_from_child = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ['-priority']

    def __str__(self):
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()


class TitleAlias(models.Model):
    alias = models.CharField(max_length=200)
    
    def __str__(self):
        return self.alias


class SpecificationTable(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    aliases = models.ManyToManyField(TitleAlias, related_name='tables')

    def __str__(self):
        return self.title


class Specification(models.Model):
    table = models.ForeignKey(SpecificationTable, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    aliases = models.ManyToManyField(TitleAlias, related_name='specs')

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Category, related_name='tagged_products')
    model = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    in_stock = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    stock_count = models.IntegerField(default=0)
    rating = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_upcoming = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-priority']


class KeyFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=500)


class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000)

class ProductImage(models.Model):
    main = models.ImageField(upload_to='product/main')
    thumbnail = models.ImageField(upload_to='product/thumbnail')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=1)
    description = models.CharField(max_length=1000)
