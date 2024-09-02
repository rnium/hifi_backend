from django.contrib import admin
from hificom import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ProductGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.CategoryGroup)
admin.site.register(models.SpecificationTable)
admin.site.register(models.Specification)
admin.site.register(models.Product)
admin.site.register(models.KeyFeature)
admin.site.register(models.ProductSpec)
admin.site.register(models.ProductImage)
admin.site.register(models.Review)
admin.site.register(models.Carousel)
admin.site.register(models.ProductCollection, ProductGroupAdmin)
admin.site.register(models.TitleAlias)
admin.site.register(models.Cart)
admin.site.register(models.CartProduct)
admin.site.register(models.Coupon)
admin.site.register(models.Order)
admin.site.register(models.WishList)