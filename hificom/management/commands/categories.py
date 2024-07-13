import yaml


main_categories = [
    {
        'title': 'Laptop',
        'slug': 'laptop',
        'priority': 5,
        'get_features_from_child': True
    },
    {
        'title': 'Desktop',
        'slug': 'desktop',
        'priority': 4,
        'get_features_from_child': True
    },
    {
        'title': 'PC Component',
        'slug': 'pc-component',
        'priority': 4,
    },
    {
        'title': 'Monitor',
        'slug': 'monitor',
        'priority': 4,
        'get_features_from_child': True
    },
    {
        'title': 'Accessories',
        'slug': 'accessories',
        'priority': 3,
    },
    {
        'title': 'Networking',
        'slug': 'networking',
        'priority': 3,
    },
    {
        'title': 'Printer',
        'slug': 'printer',
        'priority': 3,
        'get_features_from_child': True
    },
    {
        'title': 'Office Equipment',
        'slug': 'office-equipment',
        'priority': 3,
    },
    {
        'title': 'Sound System',
        'slug': 'sound-system',
        'priority': 2,
    },
    {
        'title': 'Software',
        'slug': 'software',
        'priority': 2,
    },
]

laptop_subcategories = [
    {
        'title': 'All Laptop',
        'slug': 'all-laptop',
        'priority': 3,
    },
    {
        'title': 'Gaming Laptop',
        'slug': 'gaming-laptop',
        'priority': 2,
    },
    {
        'title': 'Business Laptop',
        'slug': 'business-laptop',
        'priority': 2,
    },
    {
        'title': 'Professional Laptop',
        'slug': 'professional-laptop',
        'priority': 2,
    },
    {
        'title': 'Intel Laptop',
        'slug': 'intel-laptop',
        'priority': 1,
    },
    {
        'title': 'AMD Laptop',
        'slug': 'amd-laptop',
        'priority': 1,
    },
    {
        'title': 'Snapdragon Laptop',
        'slug': 'snapdragon-laptop',
        'priority': 1,
    },
    {
        'title': 'Accessories',
        'slug': 'laptop-accessories',
        'priority': 1,
    },
]

laptop_brands = [
    {
        'title': 'Asus',
        'slug': 'asus',
        'priority': 3,
        'cat_type': 'brand'
    },
    {
        'title': 'Lenovo',
        'slug': 'lenovo',
        'priority': 3,
        'cat_type': 'brand'
    },
    {
        'title': 'HP',
        'slug': 'hp',
        'priority': 3,
        'cat_type': 'brand'
    },
    {
        'title': 'Acer',
        'slug': 'acer',
        'priority': 2,
        'cat_type': 'brand'
    },
    {
        'title': 'Dell',
        'slug': 'dell',
        'priority': 2,
        'cat_type': 'brand'
    },
    {
        'title': 'MSI',
        'slug': 'msi',
        'priority': 2,
        'cat_type': 'brand'
    },
]

laptop_processor_types = [
    {
        'title': 'Intel Pentium & Celeron Laptop',
        'slug': 'pentium-and-celeron-laptop',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Intel Core i3',
        'slug': 'core-i3-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
    {
        'title': 'Intel Core i3',
        'slug': 'core-i3-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
    {
        'title': 'Intel Core i5',
        'slug': 'core-i5-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
    {
        'title': 'Intel Core i7',
        'slug': 'core-i7-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
    {
        'title': 'Intel Core i9',
        'slug': 'core-i9-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
    {
        'title': 'AMD Ryzen 3',
        'slug': 'ryzen-3-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
    {
        'title': 'AMD Ryzen 5',
        'slug': 'ryzen-5-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
    {
        'title': 'AMD Ryzen 7',
        'slug': 'ryzen-7-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
    {
        'title': 'AMD Ryzen 9',
        'slug': 'ryzen-9-laptop',
        'priority': 3,
        'cat_type': 'series'
    },
]

laptop_processor_models = [
    {
        'title': 'Intel Core i3-1215U',
        'slug': 'core-13-1215u',
        'priority': 0,
        'cat_type': 'series'
    }
]

laptop_processor_series = [
    {
        'title': 'Intel 10th Gen',
        'slug': 'intel-10th-gen-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Intel 11th Gen',
        'slug': 'intel-11th-gen-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Intel 12th Gen',
        'slug': 'intel-12th-gen-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Intel 13th Gen',
        'slug': 'intel-13th-gen-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Intel 14th Gen',
        'slug': 'intel-14th-gen-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Ryzen 3000 Series',
        'slug': 'ryzen-3000-series-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Ryzen 4000 Series',
        'slug': 'ryzen-4000-series-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Ryzen 5000 Series',
        'slug': 'ryzen-5000-series-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Ryzen 6000 Series',
        'slug': 'ryzen-6000-series-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Ryzen 7000 Series',
        'slug': 'ryzen-7000-series-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'Ryzen 8000 Series',
        'slug': 'ryzen-8000-series-laptop',
        'cat_type': 'tag'
    }
]

laptop_display_variants = [
    {
        'title': 'Less than 14 Inch Laptop',
        'slug': 'less-than-14-inch-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '14.1 Inch to 15 Inch Laptop',
        'slug': '14.1-inch-to-15-inch-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '15.1 Inch to 16 Inch Laptop',
        'slug': '15.1-inch-to-16-inch-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '16.1 Inch to 17 Inch Laptop',
        'slug': '16.1-inch-to-17-inch-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '17.1 Inch to 18 Inch Laptop',
        'slug': '17.1-inch-to-18-inch-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'QHD',
        'slug': 'qhd-laptop',
        'priority': 3,
        'cat_type': 'tag'
    },
    {
        'title': '2K',
        'slug': '2k-laptop',
        'priority': 3,
        'cat_type': 'tag'
    },
    {
        'title': '4K',
        'slug': '4k-laptop',
        'priority': 3,
        'cat_type': 'tag'
    },
    {
        'title': 'OLED',
        'slug': 'oled-laptop',
        'priority': 3,
        'cat_type': 'tag'
    },
    {
        'title': 'IPS Panel',
        'slug': 'ips-panel-laptop',
        'priority': 3,
        'cat_type': 'tag'
    },
]

laptop_storage_variants = [
    {
        'title': '128GB SSD Laptop',
        'slug': '128gb-ssd-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '256GB SSD Laptop',
        'slug': '256gb-ssd-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '512GB SSD Laptop',
        'slug': '512gb-ssd-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '1TB SSD Laptop',
        'slug': '1tb-ssd-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '2TB SSD Laptop',
        'slug': '2tb-ssd-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '4TB SSD Laptop',
        'slug': '4tb-ssd-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '8TB SSD Laptop',
        'slug': '8tb-ssd-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '512GB HDD Laptop',
        'slug': '512gb-hdd-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '1TB HDD Laptop',
        'slug': '1tb-hdd-laptop',
        'cat_type': 'tag'
    }
]

laptop_graphics_variants = [
    {
        'title': 'Laptop Shared Graphics',
        'slug': 'laptop-shared-graphics',
        'cat_type': 'tag'
    },
    {
        'title': '2GB Dedicated Laptop Graphics',
        'slug': '2gb-dedicated-laptop-graphics',
        'cat_type': 'tag'
    },
    {
        'title': '4GB Dedicated Laptop Graphics',
        'slug': '4gb-dedicated-laptop-graphics',
        'cat_type': 'tag'
    },
    {
        'title': '6GB Dedicated Laptop Graphics',
        'slug': '6gb-dedicated-laptop-graphics',
        'cat_type': 'tag'
    },
    {
        'title': '8GB Dedicated Laptop Graphics',
        'slug': '8gb-dedicated-laptop-graphics',
        'cat_type': 'tag'
    },
    {
        'title': '10GB Dedicated Laptop Graphics',
        'slug': '10gb-dedicated-laptop-graphics',
        'cat_type': 'tag'
    },
    {
        'title': '12GB Dedicated Laptop Graphics',
        'slug': '12gb-dedicated-laptop-graphics',
        'cat_type': 'tag'
    },
    {
        'title': '16GB Dedicated Laptop Graphics',
        'slug': '16gb-dedicated-laptop-graphics',
        'cat_type': 'tag'
    }
]

laptop_serieses = [
    {
        'title': 'Zenbook',
        'slug': 'zenbook',
        'priority': 1,
        'cat_type': 'series'
    },
    {
        'title': 'Vivobook',
        'slug': 'vivobook',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Expertbook',
        'slug': 'expertbook',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'ROG',
        'slug': 'rog',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'TUF',
        'slug': 'tuf',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Aspire',
        'slug': 'aspire',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Extensa',
        'slug': 'extensa',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Travelmate',
        'slug': 'travelmate',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Yoga',
        'slug': 'yoga',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Thinkpad',
        'slug': 'thinkpad',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Elite',
        'slug': 'elite',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Pavilion',
        'slug': 'pavilion',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Probook',
        'slug': 'probook',
        'priority': 0,
        'cat_type': 'series'
    },
    {
        'title': 'Victus',
        'slug': 'victus',
        'priority': 0,
        'cat_type': 'series'
    },
]

laptop_ram_tags = [
    {
        'title': '4GB Ram Laptop',
        'slug': '4gb-ram-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '8GB Ram Laptop',
        'slug': '8gb-ram-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '16GB Ram Laptop',
        'slug': '16gb-ram-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '32GB Ram Laptop',
        'slug': '32gb-ram-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '48GB Ram Laptop',
        'slug': '48gb-ram-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '64GB Ram Laptop',
        'slug': '64gb-ram-laptop',
        'cat_type': 'tag'
    },
    {
        'title': '128GB Ram Laptop',
        'slug': '128gb-ram-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'DDR4 Ram Laptop',
        'slug': 'ddr4-ram-laptop',
        'cat_type': 'tag'
    },
    {
        'title': 'DDR5 Ram Laptop',
        'slug': 'ddr5-ram-laptop',
        'cat_type': 'tag'
    }
]

laptop_acceesories = [
    {
        'title': 'Laptop Ram',
        'slug': 'laptop-ram',
        'priority': 3,
    },
    {
        'title': 'Laptop Battery',
        'slug': 'laptop-battery',
        'priority': 3,
    },
    {
        'title': 'Laptop Charger',
        'slug': 'laptop-charger',
        'priority': 3,
    },
    {
        'title': 'Laptop Display',
        'slug': 'laptop-display',
        'priority': 3,
    },
    {
        'title': 'Laptop Cooler',
        'slug': 'laptop-cooler',
        'priority': 3,
    },
    {
        'title': 'Laptop Backpack',
        'slug': 'laptop-backpack',
        'priority': 3,
    },
]

laptop_ram_brands = [
    {
        'title': 'Adata',
        'slug': 'adata-laptop-ram',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'Apacer',
        'slug': 'apacer-laptop-ram',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'Corsair',
        'slug': 'corsair-laptop-ram',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'HP',
        'slug': 'hp-laptop-ram',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'Netac',
        'slug': 'netac-laptop-ram',
        'cat_type': 'brand',
        'priority': 1,
    },
]

laptop_battery_brands = [
    {
        'title': 'Asus',
        'slug': 'asus-laptop-battery',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'Dell',
        'slug': 'dell-laptop-battery',
        'cat_type': 'brand',
        'priority': 1,
    },
]

monitor_brands = [
    {
        'title': 'Dahua',
        'slug': 'dahua-monitor',
        'cat_type': 'brand',
        'priority': 3,
    },
    {
        'title': 'Acer',
        'slug': 'acer-monitor',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'Hikvision',
        'slug': 'hikvision-monitor',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'MSI',
        'slug': 'msi-monitor',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'Viewsonic',
        'slug': 'viewsonic-monitor',
        'cat_type': 'brand',
        'priority': 1,
    },
    {
        'title': 'HP',
        'slug': 'hp-monitor',
        'cat_type': 'brand',
        'priority': 1,
    },
]


all_categories = [
    *main_categories,
    *laptop_subcategories,
    *laptop_brands,
    *laptop_processor_types,
    *laptop_processor_models,
    *laptop_processor_series,
    *laptop_display_variants,
    *laptop_storage_variants,
    *laptop_graphics_variants,
    *laptop_serieses,
    *laptop_ram_tags,
    *laptop_acceesories,
    *laptop_ram_brands,
    *laptop_battery_brands,
    *monitor_brands
]



with open('cat_tree.yaml') as f:
    cat_tree = yaml.load(f, yaml.SafeLoader)

with open('cat_groups.yaml') as f:
    cat_groups = yaml.load(f, yaml.SafeLoader)

