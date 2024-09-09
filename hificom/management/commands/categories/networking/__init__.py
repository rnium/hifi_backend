from .router import ROUTER_CATEGORIES, ROUTER_CATEGORY_GROUPS

main_categories = [
    {
        'title': 'Router',
        'slug': 'router',
        'priority': 3,
        'seo_title': 'Routers at HiFi Computer',
        'description': 'Enhance your network connectivity with advanced routers from HiFi Computer. Explore a range of models suitable for home and office use, offering high-speed internet access, seamless connectivity, and robust security features, available at competitive prices in Bangladesh. Choose from top brands and enjoy reliable performance for streaming, gaming, and productivity.',
    },
    {
        'title': 'WiFi Adapter',
        'slug': 'wifi-adapter',
        'priority': 3,
        'seo_title': 'WiFi Adapters at HiFi Computer',
        'description': 'Extend your wireless range and improve network performance with WiFi adapters from HiFi Computer. Explore a variety of USB and PCIe adapters compatible with desktops and laptops, offering fast and stable connections, available at competitive prices in Bangladesh. Choose from dual-band options, MU-MIMO technology, and easy installation for enhanced WiFi coverage and speed.',
    },
]
 
NETWORKING_CATEGORIES = [
     *main_categories,
     *ROUTER_CATEGORIES,
]

NETWORKING_CATEGORY_GROUPS = [
    *ROUTER_CATEGORY_GROUPS,
]