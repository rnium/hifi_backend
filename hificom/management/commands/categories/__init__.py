import yaml
from .laptop import ALL_LAPTOP_CATEGORIES, LAPTOP_GROUPS
from .main import MAIN_CATEGORIES
from .monitor import ALL_MONITOR_CATEGORIES

with open('cat_tree.yaml') as f:
    cat_tree = yaml.load(f, yaml.SafeLoader)

with open('cat_groups.yaml') as f:
    cat_groups = yaml.load(f, yaml.SafeLoader)


ALL_CATEGORIES = [
    *MAIN_CATEGORIES,
    *ALL_LAPTOP_CATEGORIES,
    *ALL_MONITOR_CATEGORIES
]

ALL_GROUPS = [
    *LAPTOP_GROUPS
]