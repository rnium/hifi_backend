from typing import Any
from .utils import main_categories
from django.core.management import BaseCommand
from hificom.models import Category


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        counts = 0
        for cat in main_categories:
            c, added = Category.objects.get_or_create(title = cat['title'])
            if added:
                cat.pop('title')
                for attr, val in cat.items():
                    setattr(c, attr, val)
                c.save()
                counts += 1
        self.stdout.write("{} category created".format(counts), self.style.SUCCESS)