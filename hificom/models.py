from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
from uuid import uuid4

User = get_user_model()

def hexcode_gen():
    return uuid4().hex

order_status_options = (
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)

class Carousel(models.Model):
    banner = models.ImageField(upload_to='features')
    site_link = models.CharField(max_length=200, null=True, blank=True)
    added_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-added_at']
  

class Category(models.Model):
    category_types = (
        ('general', 'General Category'),
        ('brand', 'Brand Category'),
        ('series', 'Series Category'),
        ('feature', 'Feature Category'),
        ('tag', 'Tag'),
    )
    display_child_types = (
        ('all', 'All Categories'),
        ('none', 'Display No Childs'),
        *category_types
    )
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=100, null=True, blank=True)
    cat_type = models.CharField(max_length=20, default='general', choices=category_types)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child_cat')
    minprice = models.FloatField(default=0)
    maxprice = models.FloatField(default=0)
    logo = models.ImageField(upload_to='category', null=True, blank=True)
    seo_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    display_childs = models.CharField(max_length=20, default='none', choices=display_child_types)
    get_features_from_child = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ['cat_type', '-priority', 'id']

    def __str__(self):
        return self.title

    
    @property
    def category_tree(self):
        cats = []
        current = self
        while current:
            cats.append(current)
            current = current.parent
        return cats[-1::-1]
    
    def update_minmax_price(self):
        product_prices = [prod.price for prod in self.tagged_products.all()]
        if product_prices:
            self.minprice = min(product_prices)
            self.maxprice = max(product_prices)
            self.save()


class CategoryGroup(models.Model):
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    root = models.ForeignKey(Category, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='groups')
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ['-priority', 'id']
    
    def __str__(self) -> str:
        return self.title
     

class TitleAlias(models.Model):
    alias = models.CharField(max_length=200)
    
    def __str__(self):
        return self.alias


class SpecificationTable(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    aliases = models.ManyToManyField(TitleAlias, related_name='tables', blank=True)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.title


class Specification(models.Model):
    table = models.ForeignKey(SpecificationTable, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    aliases = models.ManyToManyField(TitleAlias, related_name='specs', blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Category, related_name='tagged_products')
    title = models.CharField(max_length=200)
    details = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=300, unique=True, db_index=True)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    in_stock = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    stock_count = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    is_upcoming = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-priority']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class KeyFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=500, null=True, blank=True)

    @property
    def feature(self):
        if val:=self.value:
            return f"{self.title}: {val}"
        else:
            return self.title


class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    value = models.CharField(max_length=10000)


class ProductImage(models.Model):
    main = models.ImageField(upload_to='product/main', max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductCollection(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True, db_index=True)
    products = models.ManyToManyField(Product, related_name='collections')
    priority = models.IntegerField(default=0)

    class Meta:
        ordering = ['-priority', 'id']


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=1000)


class Cart(models.Model):
    cartid = models.CharField(max_length=50, unique=True, default=hexcode_gen, db_index=True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cart', 'product'], name='unique_product_in_cart')
        ]


class Coupon(models.Model):
    code = models.CharField(max_length=200, unique=True, db_index=True)
    discount_percent = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(100)], null=True, blank=True)
    max_amount = models.FloatField(null=True, blank=True)
    discount_amount = models.FloatField(validators=[MinValueValidator(1)], null=True, blank=True)
    min_spend = models.FloatField(default=0)
    max_usage = models.IntegerField(null=True, blank=True)
    expiry = models.DateTimeField()
    added_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    location_choices = (
        ('inside', 'Sylhet City'),
        ('outside', 'Outside Sylhet City'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=256, null=True)
    location = models.CharField(max_length=20, choices=location_choices)
    address = models.CharField(max_length=512)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=order_status_options, default='pending')
    added_at = models.DateField(auto_now_add=True)


class OrderStatusTimestamp(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=order_status_options, default='pending')
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['order', 'status'], name='uniqe status in an order')
        ]

