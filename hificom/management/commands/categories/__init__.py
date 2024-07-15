import yaml
from .laptop import ALL_LAPTOP_CATEGORIES, LAPTOP_GROUPS
from .main import MAIN_CATEGORIES
from .desktop import DESKTOP_CATEGORIES
from .components import PC_COMPONENT_CATEGORIES
from .monitor import ALL_MONITOR_CATEGORIES
from .accessories import ACCESSORIES_CATEGORIES
from .networking import NETWORKING_CATEGORIES
from .printer import PRINTER_CATEGORIES
from .sound_system import SOUND_SYSTEM_CATEGORIES
from .office_quipments import OFFICE_EQUIPMENT_CATEGORIES
from.softwares import SOFTWARE_CATEGORIES

with open('cat_tree.yaml') as f:
    cat_tree = yaml.load(f, yaml.SafeLoader)

with open('cat_groups.yaml') as f:
    cat_groups = yaml.load(f, yaml.SafeLoader)


ALL_CATEGORIES = [
    *MAIN_CATEGORIES,
    *ALL_LAPTOP_CATEGORIES,
    *DESKTOP_CATEGORIES,
    *PC_COMPONENT_CATEGORIES,
    *ALL_MONITOR_CATEGORIES,
    *ACCESSORIES_CATEGORIES,
    *NETWORKING_CATEGORIES,
    *PRINTER_CATEGORIES,
    *SOUND_SYSTEM_CATEGORIES,
    *OFFICE_EQUIPMENT_CATEGORIES,
    *SOFTWARE_CATEGORIES
]

ALL_GROUPS = [
    *LAPTOP_GROUPS
]