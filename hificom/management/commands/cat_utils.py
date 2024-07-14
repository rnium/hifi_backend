from hificom.models import Category, CategoryGroup
from .categories import ALL_CATEGORIES, ALL_GROUPS

class ConfigNotFoundError(BaseException):
    def __init__(self, config_type, name) -> None:
        super().__init__(f'{config_type} with name {name} Not Found')


def check_cat_tree(cat_tree):
    if type(cat_tree) == dict:
        for root in cat_tree.keys():
            check_cat_tree(cat_tree[root])
    elif type(cat_tree) == list:
        for i in cat_tree:
            if type(i) == dict:
                root = list(i.keys())[0]
                if not len(list(filter(lambda cat: cat['slug'] == root, ALL_CATEGORIES))):
                    raise ConfigNotFoundError('Category', root)
                check_cat_tree(i[root])
            elif type(i) == str:
                if not len(list(filter(lambda cat: cat['slug'] == i, ALL_CATEGORIES))):
                    raise ConfigNotFoundError('Category', i) 


def create_or_update_cat(slug, parent):
    cat_data = list(filter(lambda cat: cat['slug'] == slug, ALL_CATEGORIES))[0]
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
            if not len(list(filter(lambda group: group['slug'] == group_slug, ALL_GROUPS))):
                raise ConfigNotFoundError('Group', group_slug)
            for cat_slug in groups[root_cat_slug][group_slug]:
                if not len(list(filter(lambda cat: cat['slug'] == cat_slug, ALL_CATEGORIES))):
                    raise ConfigNotFoundError('Category', cat_slug)


def create_or_update_group(group_slug, root_cat):
    group_data = list(filter(lambda group: group['slug'] == group_slug, ALL_GROUPS))
    group = CategoryGroup.objects.filter(slug=group_slug).first()
    if not group:
        group = CategoryGroup(**group_data, root=root_cat)
        group.save()
    else:
        for attr_name, val in group_data.items():
            setattr(group, attr_name, val)
        group.parent = root_cat
        group.save()
    return group


def load_cat_groups(groups: dict):
    for root_cat_slug in groups:
        root_cat = Category.objects.get(slug=root_cat_slug)
        for group_slug in groups[root_cat_slug]:
            group = create_or_update_group(group_slug, root_cat)
            for cat_slug in groups[root_cat_slug][group_slug]:
                if not len(list(filter(lambda cat: cat['slug'] == cat_slug, ALL_CATEGORIES))):
                    raise ConfigNotFoundError('Category', cat_slug)
                

