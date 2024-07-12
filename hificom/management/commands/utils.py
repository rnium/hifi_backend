import yaml
main_categories = [
    {
        'title': 'Laptop',
        'priority': 5,
        'get_features_from_child': True
    },
    {
        'title': 'Desktop',
        'priority': 4,
        'get_features_from_child': True
    },
    {
        'title': 'PC Component',
        'priority': 4,
    },
    {
        'title': 'Monitor',
        'priority': 4,
        'get_features_from_child': True
    },
    {
        'title': 'Accessories',
        'priority': 3,
    },
    {
        'title': 'Networking',
        'priority': 3,
    },
    {
        'title': 'Printer',
        'priority': 3,
        'get_features_from_child': True
    },
    {
        'title': 'Office Equipment',
        'priority': 3,
    },
    {
        'title': 'Sound System',
        'priority': 2,
    },
    {
        'title': 'Software',
        'priority': 2,
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

laptop_serieses = [
    {
        'title': 'Zenbook',
        'slug': 'Zenbook',
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

laptop_features = [
    {
        'title': 'OLED Laptop',
        'slug': 'oled-laptop',
        'priority': 3,
        'cat_type': 'feature'
    },
    {
        'title': '4K Laptop',
        'slug': '4k-laptop',
        'priority': 3,
        'cat_type': 'feature'
    },
    {
        'title': '2K Laptop',
        'slug': '2k-laptop',
        'priority': 3,
        'cat_type': 'feature'
    },
    {
        'title': 'QHD Laptop',
        'slug': 'qhd-laptop',
        'priority': 3,
        'cat_type': 'feature'
    },
]

laptop_types = [
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
]


def traverse_cat(cat_tree, parent: str | None = None):
    if type(cat_tree) == list:
        for i in cat_tree:
            if type(i) == dict:
                root = list(i.keys())[0]
                print(f"{parent} -> {root}")
                traverse_cat(i[root], root)
            elif type(i) == str:
                print(f"{parent} -> {i}")

def browse_yaml(tree):
    for root in tree.keys():
        traverse_cat(tree[root], root)

with open('cat_tree.yaml') as f:
    tree = yaml.load(f, yaml.SafeLoader)
    


if __name__ == "__main__":
    browse_yaml(tree)