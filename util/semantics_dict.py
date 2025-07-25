from collections import defaultdict

# Default value if key not found
default_semantic = 0
default_color = (0, 0, 0)
default_label = 'no_type'

# Original dictionaries wrapped in defaultdict
semantics_dict = defaultdict(lambda: default_semantic, {
    'living_room': 1,
    'kitchen': 2,
    'bedroom': 3,
    'bathroom': 4,
    'restroom': 5,
    'balcony': 6,
    'closet': 7,
    'corridor': 8,
    'washing_room': 9,
    'PS': 10,
    'outside': 11,
    'wall': 12,
    'no_type': 0
})

semantics_dict_rev = defaultdict(lambda: default_label, {
    0: 'no_type', 1: 'living_room', 2: 'kitchen', 3: 'bedroom',
    4: 'bathroom', 5: 'restroom', 6: 'balcony', 7: 'closet',
    8: 'corridor', 9: 'washing_room', 10: 'PS', 11: 'outside',
    12: 'wall'
})

semantics_dict_color = defaultdict(lambda: default_color, {
    'living_room': (0, 0, 220),
    'kitchen': (0, 220, 220),
    'bedroom': (0, 220, 0),
    'bathroom': (220, 220, 0),
    'restroom': (220, 0, 0),
    'balcony': (220, 0, 220),
    'closet': (110, 0, 110),
    'corridor': (110, 0, 0),
    'washing_room': (0, 0, 110),
    'PS': (0, 110, 110),
    'outside': (0, 0, 0),
    'wall': (110, 110, 110),
    'no_type': (20, 20, 20)
})
