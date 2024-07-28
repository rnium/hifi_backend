from typing import Any
from django.core.management import BaseCommand
from hificom.models import Category


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        categories = Category.objects.all()
        for cat in categories:
            product_prices = [prod.price for prod in cat.tagged_products.all()]
            if product_prices:
                cat.minprice = min(product_prices)
                cat.maxprice = max(product_prices)
                cat.save()
        self.stdout.write('Category minmax prices updated!', self.style.SUCCESS)
