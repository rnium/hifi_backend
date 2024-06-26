from django.contrib import admin
from hificom import models
# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.SpecificationTable)
admin.site.register(models.Specification)
admin.site.register(models.Product)
admin.site.register(models.KeyFeature)
admin.site.register(models.ProductSpec)
admin.site.register(models.ProductImage)
admin.site.register(models.Review)
admin.site.register(models.Carousel)