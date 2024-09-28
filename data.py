import random

# Convert menu items to a list of dictionaries with stock numbers for non-drinks
menu_items = [
    {'code': 'D1', 'name': 'SODA', 'price': 3, 'stock': float('inf')},
    {'code': 'D2', 'name': 'LEMONADE', 'price': 3, 'stock': float('inf')},
    {'code': 'D3', 'name': 'TEA', 'price': 2, 'stock': float('inf')},
    {'code': 'D4', 'name': 'WATER', 'price': 0, 'stock': float('inf')},
    {'code': 'A1', 'name': 'POTATO_CAKES', 'price': 7, 'stock': random.randint(25, 50)},
    {'code': 'A2', 'name': 'SPINACH_DIP', 'price': 5, 'stock': random.randint(25, 50)},
    {'code': 'A3', 'name': 'OYSTERS', 'price': 13, 'stock': random.randint(25, 50)},
    {'code': 'A4', 'name': 'CHEESE_FRIES', 'price': 4, 'stock': random.randint(25, 50)},
    {'code': 'A5', 'name': 'ONION_RINGS', 'price': 7, 'stock': random.randint(25, 50)},
    {'code': 'S1', 'name': 'COBB', 'price': 14, 'stock': random.randint(25, 50)},
    {'code': 'S2', 'name': 'CAESAR', 'price': 13, 'stock': random.randint(25, 50)},
    {'code': 'S3', 'name': 'GREEK', 'price': 12, 'stock': random.randint(25, 50)},
    {'code': 'E1', 'name': 'BURGER', 'price': 16, 'stock': random.randint(25, 50)},
    {'code': 'E2', 'name': 'PASTA', 'price': 15, 'stock': random.randint(25, 50)},
    {'code': 'E3', 'name': 'GNOCCHI', 'price': 14, 'stock': random.randint(25, 50)},
    {'code': 'E4', 'name': 'GRILLED_STEAK_SANDWICH', 'price': 17, 'stock': random.randint(25, 50)},
    {'code': 'T1', 'name': 'CARAMEL_CHEESECAKE', 'price': 13, 'stock': random.randint(25, 50)},
    {'code': 'T2', 'name': 'APPLE_COBBLER', 'price': 12, 'stock': random.randint(25, 50)},
    {'code': 'T3', 'name': 'BROWNIE_SUNDAE', 'price': 9, 'stock': random.randint(25, 50)},
    {'code': 'T4', 'name': 'FLAN', 'price': 8, 'stock': random.randint(25, 50)},
]

drink_items = ['D1', 'D2', 'D3', 'D4']
appetizer_items = ['A1', 'A2', 'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2', 'E3', 'E4']
dessert_items = ['T1', 'T2', 'T3', 'T4']
all_items = drink_items + appetizer_items + salad_items + entree_items + dessert_items
