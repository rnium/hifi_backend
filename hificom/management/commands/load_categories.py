from typing import Any
from .cat_utils import load_cat_tree, check_cat_tree, CategoryConfigNotFoundError
from django.core.management import BaseCommand
from hificom.models import Category
from .categories import cat_tree


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        try:
            check_cat_tree(cat_tree)
        except CategoryConfigNotFoundError as e:
            self.stdout.write("{}".format(str(e)), self.style.ERROR)
        except Exception as e:
            self.stdout.write("Tree check failded. Details: {}".format(str(e)), self.style.ERROR)
        load_cat_tree(cat_tree)
        self.stdout.write("Categories loaded", self.style.SUCCESS)