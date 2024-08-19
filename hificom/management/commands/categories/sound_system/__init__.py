from .headphone import HEADPHONE_CATEGORIES, HEADPHONE_CATEGORY_GROUPS

main_categories = [
    {
        'title': 'Headphone',
        'slug': 'headphones',
        'priority': 5,
        'seo_title': 'Headphones at HiFi Computer',
        'description': 'Enjoy personal audio excellence with premium headphones from HiFi Computer. Explore wireless, noise-cancelling, and gaming headphones designed for comfort and superior sound quality. Available at competitive prices in Bangladesh, our headphones feature ergonomic designs, long-lasting battery life, and advanced audio technologies for immersive listening experiences.',
    },
    {
        'title': 'Earphones',
        'slug': 'earphone',
        'priority': 5,
        'seo_title': 'Earphones at HiFi Computer',
        'description': 'Discover superior sound quality and comfort with our range of earphones at HiFi Computer. From wireless to noise-cancelling options, our earphones offer exceptional audio performance and stylish design. Available at competitive prices in Bangladesh, they are perfect for everyday use, delivering a seamless listening experience with advanced features and durable build.'
    }
    ,
    {
        'title': 'Speakers',
        'slug': 'speaker-system',
        'priority': 2,
        'seo_title': 'Speaker Systems at HiFi Computer',
        'description': 'Elevate your audio setup with high-performance speaker systems from HiFi Computer. Explore stereo speakers, surround sound systems, and portable Bluetooth speakers for home entertainment and on-the-go use. Available at competitive prices in Bangladesh, our speaker systems deliver clear, immersive sound for music, movies, and gaming.',
    },
    {
        'title': 'Microphone',
        'slug': 'microphone',
        'priority': 2,
        'seo_title': 'Speaker Systems at HiFi Computer',
        'description': 'Elevate your audio setup with high-performance speaker systems from HiFi Computer. Explore stereo speakers, surround sound systems, and portable Bluetooth speakers for home entertainment and on-the-go use. Available at competitive prices in Bangladesh, our speaker systems deliver clear, immersive sound for music, movies, and gaming.',
    },
]

SOUND_SYSTEM_CATEGORIES = [
    *main_categories,
    *HEADPHONE_CATEGORIES,
]


SOUND_SYSTEM_GROUPS = [
    *HEADPHONE_CATEGORY_GROUPS
]