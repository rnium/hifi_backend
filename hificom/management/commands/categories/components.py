from .motherboard import ALL_MOTHERBOARD_CATEGORIES, MOTHERBOARD_CATEGORY_GROUPS

main_component_categories = [
    {
        'title': 'Processor',
        'slug': 'processor',
        'priority': 4,
        'seo_title': 'Processors at HiFi Computer',
        'description': 'Upgrade your PC\'s performance with the latest processors from HiFi Computer. Discover a wide selection of CPUs designed for gaming, content creation, and everyday computing needs, available at competitive prices in Bangladesh. Choose from top brands and enjoy enhanced speed and efficiency for your tasks.',
    },
    {
        'title': 'RAM',
        'slug': 'ram',
        'priority': 4,
        'seo_title': 'RAM at HiFi Computer',
        'description': 'Boost your PC\'s multitasking capabilities with high-performance RAM from HiFi Computer. Explore a variety of memory modules suitable for gaming, professional applications, and everyday use, available at competitive prices in Bangladesh. Upgrade your system\'s memory capacity and experience smoother performance across applications.',
    },
    {
        'title': 'Motherboard',
        'slug': 'motherboard',
        'priority': 4,
        'seo_title': 'RAM at HiFi Computer',
        'description': 'Boost your PC\'s multitasking capabilities with high-performance RAM from HiFi Computer. Explore a variety of memory modules suitable for gaming, professional applications, and everyday use, available at competitive prices in Bangladesh. Upgrade your system\'s memory capacity and experience smoother performance across applications.',
    },
    {
        'title': 'PC Casing',
        'slug': 'pc-casing',
        'priority': 3,
        'seo_title': 'PC Casings at HiFi Computer',
        'description': 'Enhance the aesthetics and functionality of your PC with stylish casings from HiFi Computer. Discover a range of designs and sizes to accommodate different builds and preferences, available at competitive prices in Bangladesh. Choose durable materials and innovative features for optimal airflow and component protection.',
    },
    {
        'title': 'Power Supply',
        'slug': 'power-supply',
        'priority': 3,
        'seo_title': 'Power Supplies at HiFi Computer',
        'description': 'Ensure reliable power delivery for your PC setup with high-quality power supplies from HiFi Computer. Explore efficient and stable PSU options suitable for gaming rigs, workstations, and custom builds, available at competitive prices in Bangladesh. Choose from trusted brands and wattage options to meet your system\'s power requirements.',
    },
]

PC_COMPONENT_CATEGORIES = [
    *main_component_categories,
    *ALL_MOTHERBOARD_CATEGORIES
]

PC_COMPONENT_CATEGORY_GROUPS = [
    *MOTHERBOARD_CATEGORY_GROUPS
]