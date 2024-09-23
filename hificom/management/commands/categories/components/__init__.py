from .motherboard import ALL_MOTHERBOARD_CATEGORIES, MOTHERBOARD_CATEGORY_GROUPS
from .pc_casing import PC_CASING_CATEGORIES, PC_CASING_CATEGORY_GROUPS
from .power_supply import POWER_SUPPLY_CATEGORIES, POWER_SUPPLY_CATEGORY_GROUPS
from .storage import STORAGE_CATEGORIES, STORAGE_GROUPS
from .desktop_ram import DESKTOP_RAM_CATEGORIES, DESKTOP_RAM_GROUPS
from .processor import PROCESSOR_CATEGORIES, PROCESSOR_GROUPS

main_component_categories = [
    {
        'title': 'Processor',
        'slug': 'processor',
        'priority': 4,
        'seo_title': 'Processors at HiFi Computer',
        'description': 'Upgrade your PC\'s performance with the latest processors from HiFi Computer. Discover a wide selection of CPUs designed for gaming, content creation, and everyday computing needs, available at competitive prices in Bangladesh. Choose from top brands and enjoy enhanced speed and efficiency for your tasks.',
    },
    {
        'title': 'Desktop RAM',
        'slug': 'ram',
        'priority': 4,
        'seo_title': 'Desktop RAM at HiFi Computer',
        'description': 'Boost your PC\'s multitasking capabilities with high-performance Desktop RAM from HiFi Computer. Explore a variety of memory modules suitable for gaming, professional applications, and everyday use, available at competitive prices in Bangladesh. Upgrade your system\'s memory capacity and experience smoother performance across applications.',
    },
    {
        'title': 'Motherboard',
        'slug': 'motherboard',
        'priority': 4,
        'seo_title': 'Motherboards at HiFi Computer',
        'description': 'Discover a wide range of high-performance motherboards at HiFi Computer, perfect for gaming, professional applications, and everyday computing needs. Our selection includes top brands and the latest models, ensuring you find the perfect motherboard to enhance your PC\'s performance. Enjoy competitive prices and convenient doorstep delivery across Bangladesh. Upgrade your system with a reliable motherboard from HiFi Computer today.'
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
    {
        'title': 'Storage',
        'slug': 'storage',
        'priority': 3,
        'seo_title': 'Storage Solutions at HiFi Computer',
        'description': 'Upgrade your system\'s performance with top-notch storage solutions from HiFi Computer. Discover a wide range of SSDs and HDDs designed for reliability and speed, perfect for boosting your PC’s storage capacity and efficiency. Whether you need high-speed SSDs for quick access or ample HDDs for large data storage, find the best options at competitive prices in Bangladesh. Choose from trusted brands and enhance your computing experience with our storage solutions.'
    }
]

PC_COMPONENT_CATEGORIES = [
    *main_component_categories,
    *ALL_MOTHERBOARD_CATEGORIES,
    *PC_CASING_CATEGORIES,
    *POWER_SUPPLY_CATEGORIES,
    *STORAGE_CATEGORIES,
    *DESKTOP_RAM_CATEGORIES,
    *PROCESSOR_CATEGORIES,
]

PC_COMPONENT_CATEGORY_GROUPS = [
    *MOTHERBOARD_CATEGORY_GROUPS,
    *PC_CASING_CATEGORY_GROUPS,
    *POWER_SUPPLY_CATEGORY_GROUPS,
    *STORAGE_GROUPS,
    *DESKTOP_RAM_GROUPS,
    *PROCESSOR_GROUPS,
]