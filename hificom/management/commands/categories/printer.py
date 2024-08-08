printer_brands = [
    {
        'title': 'Epson',
        'slug': 'epson-printer',
        'priority': 4,
        'seo_title': 'Epson Printers at HiFi Computer',
        'description': 'Experience outstanding print quality and efficiency with Epson printers from HiFi Computer. Choose from a range of models designed for home, office, and commercial use, featuring high-speed printing, vibrant color reproduction, and convenient wireless connectivity. Epson printers provide reliable performance and innovative features at competitive prices in Bangladesh, making them a top choice for all your printing needs.'
    },
    {
        'title': 'Pantum',
        'slug': 'pantum-printer',
        'priority': 5,
        'seo_title': 'Pantum Printers at HiFi Computer',
        'description': 'Explore durable and cost-effective printing solutions with Pantum printers from HiFi Computer. Ideal for both home and office environments, Pantum printers offer robust performance, high-speed printing, and user-friendly features. Available at competitive prices in Bangladesh, Pantum printers deliver reliable quality and efficiency for all your printing tasks.'
    },
    {
        'title': 'Brother',
        'slug': 'brother-printer',
        'priority': 3,
        'seo_title': 'Brother Printers at HiFi Computer',
        'description': 'Explore reliable printing solutions with Brother printers from HiFi Computer. Discover a variety of models suitable for home and office use, offering efficient performance, high-quality prints, and innovative features like wireless connectivity and duplex printing. Available at competitive prices in Bangladesh, Brother printers deliver exceptional reliability and cost-effectiveness.',
    },
    {
        'title': 'HP',
        'slug': 'hp-printer',
        'priority': 3,
        'seo_title': 'HP Printers at HiFi Computer',
        'description': 'Experience superior printing quality and versatility with HP printers from HiFi Computer. Choose from a range of models designed for home, office, and business environments, featuring advanced printing technologies, mobile printing capabilities, and energy-efficient operation. Available at competitive prices in Bangladesh, HP printers deliver reliable performance and professional-quality prints.',
    },
    {
        'title': 'Canon',
        'slug': 'canon-printer',
        'priority': 3,
        'seo_title': 'Canon Printers at HiFi Computer',
        'description': 'Discover exceptional printing precision and reliability with Canon printers from HiFi Computer. Explore a variety of models suitable for photography, home office, and professional printing needs, offering high-resolution output, versatile media handling, and wireless connectivity options. Available at competitive prices in Bangladesh, Canon printers combine performance, innovation, and eco-conscious features.',
    },
]

printer_type = [
    {
        'title': 'Ink',
        'slug': 'ink-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Inkjet',
        'slug': 'inkjet-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Thermal Inkjet',
        'slug': 'thermal-inkjet-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Inktank',
        'slug': 'inktank-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Laser',
        'slug': 'laser-printer',
        'cat_type': 'tag',
        'priority': 4
    }
]

printer_extra_functionality = [
    {
        'title': 'Scan/Copy',
        'slug': 'scan-copy-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Scan/Copy/Fax',
        'slug': 'scan-copy-fax-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Professional Photo',
        'slug': 'professional-photo-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Duplex',
        'slug': 'duplex-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Networking Interface',
        'slug': 'printer-w-networking-interface',
        'cat_type': 'tag',
        'priority': 4
    }
]

printer_color_output = [
    {
        'title': 'Color',
        'slug': 'color-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Black & White',
        'slug': 'black-and-white-printer',
        'cat_type': 'tag',
        'priority': 4
    },
    {
        'title': 'Color + Black & White',
        'slug': 'color-and-black-and-white-printer',
        'cat_type': 'tag',
        'priority': 4
    }
]


PRINTER_CATEGORIES = [
    *printer_brands,
    *printer_type,
    *printer_extra_functionality,
    *printer_color_output,
]


PRINTER_GROUPS = [
    {
        'title': 'Printer Type',
        'slug': 'printer-type',
        'priority': 4
    },
    {
        'title': 'Color Output',
        'slug': 'printer-color-output',
        'priority': 4
    },
    {
        'title': 'Extra Functionality',
        'slug': 'printer-extra-functionality',
        'priority': 4
    },
]