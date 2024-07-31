from typing import Any
from django.core.management import BaseCommand
from hificom.models import Category


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        categories = Category.objects.all()
        for cat in categories:
            cat.update_minmax_price()
        self.stdout.write('Category minmax prices updated!', self.style.SUCCESS)
