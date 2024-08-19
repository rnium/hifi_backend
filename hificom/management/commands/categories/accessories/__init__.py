from .keyboard import KEYBOARD_CATEGORIES, KEYBOARD_CATEGORY_GROUPS
from .mouse import MOUSE_CATEGORIES, MOUSE_CATEGORY_GROUPS

main_categories = [
    {
        'title': 'Keyboard',
        'slug': 'keyboard',
        'priority': 10,
        'seo_title': 'Keyboards at HiFi Computer',
        'description': 'Enhance your typing experience with ergonomic keyboards from HiFi Computer. Discover a variety of mechanical, membrane, and wireless keyboards tailored for gaming, office work, and everyday use, available at competitive prices in Bangladesh. Choose from top brands and enjoy customizable features to suit your preferences and workflow.',
    },
    {
        'title': 'Mouse',
        'slug': 'mouse',
        'priority': 10,
        'seo_title': 'Mice at HiFi Computer',
        'description': 'Navigate your digital tasks with precision using advanced mice from HiFi Computer. Explore a range of wired and wireless options designed for gaming, productivity, and creative applications, available at competitive prices in Bangladesh. Choose ergonomic designs, adjustable DPI settings, and programmable buttons for enhanced control and comfort.',
    },
    {
        'title': 'UPS',
        'slug': 'ups',
        'priority': 3,
        'seo_title': 'UPS at HiFi Computer',
        'description': 'Protect your devices from power interruptions with reliable UPS solutions from HiFi Computer. Explore uninterruptible power supplies designed to safeguard your equipment during outages, fluctuations, and surges, available at competitive prices in Bangladesh. Choose from various capacities and features to ensure uninterrupted operation for your home or office setup.',
    },
]


ACCESSORIES_CATEGORIES = [
    *main_categories,
    *KEYBOARD_CATEGORIES,
    *MOUSE_CATEGORIES,
]


ACCESSORIES_CATEGORY_GROUPS = [
    *KEYBOARD_CATEGORY_GROUPS,
    *MOUSE_CATEGORY_GROUPS,
]
