#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data

def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  for item in data.menu_items:
    if item['code'] == item_code:
      return item['name'], item['price'], item['stock']
  print('Item not found')
  return None, None, None
def display_items():
  print('Drinks:', [(item['name'], item['code']) for item in data.menu_items if item['code'] in data.drink_items])
  print('Appetizers:', [(item['name'], item['code']) for item in data.menu_items if item['code'] in data.appetizer_items])
  print('Salads:', [(item['name'], item['code']) for item in data.menu_items if item['code'] in data.salad_items])
  print('Entrees:', [(item['name'], item['code']) for item in data.menu_items if item['code'] in data.entree_items])
  print('Desserts:', [(item['name'], item['code']) for item in data.menu_items if item['code'] in data.dessert_items])

def get_item_number():
  while True:
   display_items()
   order_item = input('Enter dish number and quantity: ').split()
   if len(order_item) == 2:
    item_code, quantity = order_item
    item_name, item_price, stock = get_item_information(item_code)
    if item_name and int(quantity) <= stock:
      return item_code, int(quantity)
    elif item_name:
      print(f"Only {stock} {item_name}(s) left. Please adjust your quantity.")
    else:
      print("Invalid item code. Try again.")
  else:
    print("Invalid input. Enter both dish number and quantity.")

def print_check(order):
    print("\nYour Order Summary:")
    total = 0
    for item_name, item_price, quantity in order:
        extended_price = item_price * quantity
        total += extended_price
        print(f"{item_name} (x{quantity}) - ${extended_price}")

    tax = total * 0.07  # Assuming 7% tax
    grand_total = total + tax
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")
    print("Thank you for dining with us!\n")

def reset_order():
  print("your order has been reset.")
  return[] 

def display_current_order(order):
    if not order:
        print("Your order is empty.")
        return
    print("\nCurrent Order:")
    for idx, (item_name, item_price, quantity) in enumerate(order, start=1):
        print(f"{idx}. {item_name} (x{quantity}) - ${item_price * quantity:.2f}")

def update_menu():
    """Manager function to update the menu (add, remove, update items)."""
    while True:
        print("\nManager Menu Options:")
        print("1. Add a new item")
        print("2. Remove an item")
        print("3. Update item price or stock")
        print("4. Go back")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
          code = input("Enter item code: ").upper()
          name = input("Enter item name: ")
          item_exists = False
          for item in data.menu_items:
            if item['code'] == code or item['name'] == name:
              item_exists = True
              break
          if item_exists:
            print(f"Item with code '{code}' or name '{name}' already exists.")
            continue
          else:
            # If item does not exist, get price and stock and add it to the menu
            price = int(input("Enter item price: "))
            stock = input("Enter item stock (for drinks, enter 'inf'): ")
            if stock == 'inf':
              stock = float('inf')  # Unlimited stock for drinks
            else:
              stock = int(stock)
          
            data.menu_items.append({'code': code, 'name': name, 'price': price, 'stock': stock})
            print(f"Item {name} added successfully.")
            
        elif choice == "2":
          code = input("Enter item code to remove: ").upper()
          data.menu_items = [item for item in data.menu_items if item['code'] != code]
          print(f"Item with code {code} removed successfully.")
            
        elif choice == "3":
          code = input("Enter item code to update: ").upper()
          for item in data.menu_items:
            if item['code'] == code:
              new_price = int(input(f"Enter new price for {item['name']} (current: ${item['price']}): "))
              new_stock = input(f"Enter new stock for {item['name']} (current: {item['stock']}): ")
              new_stock = float('inf') if new_stock == 'inf' else int(new_stock)
              item['price'], item['stock'] = new_price, new_stock
              print(f"Item {item['name']} updated successfully.")
              break
            
          print("Item code not found.")
                
        elif choice == "4":
          break
        else:
          print("Invalid input. Try again.")