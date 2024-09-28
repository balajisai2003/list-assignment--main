#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  print(item_code)
  for item in data.menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return item_name.encode("ascii", "ignore").decode(), int(item_price)

def display_items():
  print('Drinks', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'D'])
  print('Appetizers', [a.replace('\u200b','') for a in data.menu_items if a[0] == 'A'])
  print("Salads:", [s.replace('\u200b','') for s in data.menu_items if s[0] == 'S'])
  print("Entrees:", [e.replace('\u200b','') for e in data.menu_items if e[0] == 'E'])
  print("Desserts:", [t.replace('\u200b','') for t in data.menu_items if t[0] == 'T'])

def get_item_number():
  while True:
   display_items()
   order_item = input('Enter dish number and quantity: ')
   parts = order_item.split()
   if len(parts) == 2:  # Check if there are exactly two parts
      item_code, quantity = parts
      if item_code in data.all_items and quantity.isdigit():  # Check if item code is valid and quantity is a digit
         return item_code, int(quantity)  # Return the item code and quantity as integer
      else:
         print("Invalid dish number or quantity. Please try again.")
   else:
     print("Please enter both dish number and quantity, separated by a space.")

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
            price = int(input("Enter item price: "))
            stock = int(input("Enter item stock (for drinks, enter 'inf'): "))
            stock = float('inf') if stock == 'inf' else stock
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
            else:
                print("Item code not found.")
                
        elif choice == "4":
            break
        else:
            print("Invalid input. Try again.")