from typing import Any
from .cat_utils import load_cat_tree, load_cat_groups, check_cat_tree, check_cat_groups, ConfigNotFoundError
from django.core.management import BaseCommand
from hificom.models import Category
from .categories import cat_tree, cat_groups


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        try:
            check_cat_tree(cat_tree)
        except ConfigNotFoundError as e:
            self.stdout.write("Tree check failded. Details: {}".format(str(e)), self.style.ERROR)
        except Exception as e:
            self.stdout.write("Tree check failded. Details: {}".format(str(e)), self.style.ERROR)
            return
        try:
            check_cat_groups(cat_groups)
        except ConfigNotFoundError as e:
            self.stdout.write("Category group checking failded. Details: {}".format(str(e)), self.style.ERROR)
        except Exception as e:
            self.stdout.write("Category group checking failded. Details: {}".format(str(e)), self.style.ERROR)
            return
        load_cat_tree(cat_tree)
        load_cat_groups(cat_groups)
        self.stdout.write("Categories & Groups Loaded", self.style.SUCCESS)

