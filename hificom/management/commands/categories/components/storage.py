from .storage__ssd import SSD_CATEGORIES, SSD_GROUPS
from .storage__hdd import HDD_CATEGORIES, HDD_GROUPS

storage_types = [
    {
        'title': 'SSD',
        'slug': 'ssd',
        'priority': 5,
        'cat_type': 'general',
        'seo_title': 'Solid State Drive at HiFi Computer',
        'description': (
            'Upgrade your computer\'s performance with SSDs from HiFi Computer. '
            'Solid State Drives (SSDs) offer faster data access, quicker boot times, '
            'and improved reliability compared to traditional hard drives. Whether '
            'you\'re a gamer, content creator, or everyday user, our SSDs provide '
            'the speed and durability you need. Explore a variety of SSDs available '
            'at competitive prices in Bangladesh.'
        )
    },
    {
        'title': 'HDD',
        'slug': 'hdd',
        'priority': 5,
        'cat_type': 'general',
        'seo_title': 'Hard Drive at HiFi Computer',
        'description': (
            'Store all your data securely with HDDs from HiFi Computer. Hard Disk Drives '
            '(HDDs) offer large storage capacities at affordable prices, making them ideal '
            'for backups, media libraries, and general data storage. Whether you need a high-capacity '
            'drive for work or personal use, we have a range of HDDs that deliver reliable performance. '
            'Shop now at competitive prices in Bangladesh.'
        )
    }
]

STORAGE_CATEGORIES = [
    *storage_types,
    *SSD_CATEGORIES,
    *HDD_CATEGORIES,
]

STORAGE_GROUPS = [
    *SSD_GROUPS,
    *HDD_GROUPS,
]