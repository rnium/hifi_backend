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

if __name__ == "__main__":
    print(len(list(filter(lambda i: i['priority'] > 2, main_categories))))