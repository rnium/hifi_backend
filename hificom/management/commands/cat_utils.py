from hificom.models import Category
from .categories import all_categories

class CategoryConfigNotFoundError(BaseException):
    def __init__(self, name) -> None:
        super().__init__(f'{name} Not Found')


def check_cat_tree(cat_tree):
    if type(cat_tree) == dict:
        for root in cat_tree.keys():
            check_cat_tree(cat_tree[root])
    elif type(cat_tree) == list:
        for i in cat_tree:
            if type(i) == dict:
                root = list(i.keys())[0]
                if not len(list(filter(lambda cat: cat['slug'] == root, all_categories))):
                    raise CategoryConfigNotFoundError(root)
                check_cat_tree(i[root])
            elif type(i) == str:
                if not len(list(filter(lambda cat: cat['slug'] == i, all_categories))):
                    raise CategoryConfigNotFoundError(i) 


def create_or_update_cat(slug, parent):
    cat_data = list(filter(lambda cat: cat['slug'] == slug, all_categories))[0]
    cat = Category.objects.filter(slug=slug).first()
    if cat:
        for attr_name, val in cat_data.items():
            setattr(cat, attr_name, val)
        cat.parent = parent
        cat.save()
    else:
        cat = Category(**cat_data, parent=parent)
        cat.save()
    return cat


def load_cat_tree(tree, parent = None):
    if type(tree) == dict:
        for root in tree.keys():
            cat = create_or_update_cat(root, parent)
            load_cat_tree(tree[root], cat)
    elif type(tree) == list:
        for i in tree:
            if type(i) == dict:
                cat_slug = list(i.keys())[0]
                cat = create_or_update_cat(cat_slug, parent)
                load_cat_tree(i[cat_slug], cat)
            elif type(i) == str:
                create_or_update_cat(i, parent)


def check_cat_groups(groups: dict):
    for root_cat_slug in groups:
        for group_slug in groups[root_cat_slug]:
            for cat_slug in groups[root_cat_slug][group_slug]:
                if not len(list(filter(lambda cat: cat['slug'] == cat_slug, all_categories))):
                    raise CategoryConfigNotFoundError(cat_slug)