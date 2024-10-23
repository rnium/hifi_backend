from .keyboard import KEYBOARD_CATEGORIES, KEYBOARD_CATEGORY_GROUPS
from .mouse import MOUSE_CATEGORIES, MOUSE_CATEGORY_GROUPS
from .ups import UPS_CATEGORIES, UPS_CATEGORY_GROUPS

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
        'priority': 9,
        'seo_title': 'UPS at HiFi Computer',
        'description': 'Protect your devices from power interruptions with reliable UPS solutions from HiFi Computer. Explore uninterruptible power supplies designed to safeguard your equipment during outages, fluctuations, and surges, available at competitive prices in Bangladesh. Choose from various capacities and features to ensure uninterrupted operation for your home or office setup.',
    },
    {
        'title': 'Mini UPS',
        'slug': 'mini-ups',
        'priority': 4,
        'seo_title': 'Mini UPS at HiFi Computer',
        'description': 'Ensure uninterrupted power supply with compact and efficient mini UPS devices, perfect for routers and small electronic devices.',
    },
    {
        'title': 'UPS Battery',
        'slug': 'ups-battery',
        'priority': 4,
        'seo_title': 'UPS Batteries at HiFi Computer',
        'description': 'Find reliable UPS batteries to keep your systems running during power outages, ensuring continuous operation.',
    },
    {
        'title': 'Power Strip',
        'slug': 'power-strip',
        'priority': 4,
        'seo_title': 'Power Strips at HiFi Computer',
        'description': 'Organize your electronic devices with durable power strips offering surge protection and multiple outlets.',
    },
    {
        'title': 'Power Bank',
        'slug': 'power-bank',
        'priority': 4,
        'seo_title': 'Power Banks at HiFi Computer',
        'description': 'Charge your devices on the go with high-capacity power banks, ensuring you never run out of power.',
    },
    {
        'title': 'Power Cable',
        'slug': 'power-cable',
        'priority': 4,
        'seo_title': 'Power Cables at HiFi Computer',
        'description': 'Browse through a selection of durable power cables designed to provide reliable connections for your devices.',
    },
    {
        'title': 'USB Hub',
        'slug': 'usb-hub',
        'priority': 4,
        'seo_title': 'USB Hubs at HiFi Computer',
        'description': 'Expand your connectivity with USB hubs, offering multiple ports for charging and data transfer.',
    },
    {
        'title': 'Wireless Charger',
        'slug': 'wireless-charger',
        'priority': 4,
        'seo_title': 'Wireless Chargers at HiFi Computer',
        'description': 'Charge your devices wirelessly with fast and efficient wireless chargers, compatible with a wide range of devices.',
    },
    {
        'title': 'Car Charger',
        'slug': 'car-charger',
        'priority': 4,
        'seo_title': 'Car Chargers at HiFi Computer',
        'description': 'Keep your devices powered up on the road with compact and fast-charging car chargers.',
    },
    {
        'title': 'Wall Charger',
        'slug': 'wall-charger',
        'priority': 4,
        'seo_title': 'Wall Chargers at HiFi Computer',
        'description': 'Find reliable and fast wall chargers for smartphones, tablets, and other electronic devices.',
    },
    {
        'title': 'Phone Holder',
        'slug': 'phone-holder',
        'priority': 4,
        'seo_title': 'Phone Holders at HiFi Computer',
        'description': 'Secure your phone while driving or working with sturdy and adjustable phone holders.',
    },
    {
        'title': 'Selfie Stick',
        'slug': 'selfie-stick',
        'priority': 4,
        'seo_title': 'Selfie Sticks at HiFi Computer',
        'description': 'Capture perfect selfies and group photos with extendable and portable selfie sticks.',
    },
    {
        'title': 'Cable Organizer',
        'slug': 'cable-organizer',
        'priority': 4,
        'seo_title': 'Cable Organizers at HiFi Computer',
        'description': 'Keep your cables neat and tangle-free with practical and easy-to-use cable organizers.',
    },
    {
        'title': 'Screen Cleaner',
        'slug': 'screen-cleaner',
        'priority': 4,
        'seo_title': 'Screen Cleaners at HiFi Computer',
        'description': 'Ensure a spotless and streak-free display with effective and safe screen cleaners.',
    },
    {
        'title': 'Blower Machine',
        'slug': 'blower-machine',
        'priority': 4,
        'seo_title': 'Blower Machines at HiFi Computer',
        'description': 'Keep your electronics dust-free with powerful blower machines designed for cleaning sensitive components.',
    },
]


ACCESSORIES_CATEGORIES = [
    *main_categories,
    *KEYBOARD_CATEGORIES,
    *MOUSE_CATEGORIES,
    *UPS_CATEGORIES,
]


ACCESSORIES_CATEGORY_GROUPS = [
    *KEYBOARD_CATEGORY_GROUPS,
    *MOUSE_CATEGORY_GROUPS,
    *UPS_CATEGORY_GROUPS,
]
