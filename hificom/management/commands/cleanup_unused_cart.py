from typing import Any
from django.utils import timezone
from django.conf import settings
from django.db.models import Count
from django.core.management import BaseCommand
from hificom.models import Cart


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        # Clean up dangling carts that has no products and are older than the specified lifetime
        old_carts = Cart.objects.filter(
            added_at__lt=timezone.now() - settings.DANGLING_CART_LIFETIME,
            checked_out=False
        )
        dangling_carts = old_carts.annotate(num_products=Count('cartproduct')).filter(num_products=0)
        num_dangling_carts = dangling_carts.count()
        dangling_carts.delete()
        self.stdout.write(
            self.style.SUCCESS(f'Successfully cleaned up {num_dangling_carts} dangling carts')
        )
