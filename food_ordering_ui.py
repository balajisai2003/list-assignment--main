#user interface to the main menu
import data
import functions
def show_main_menu():
  order = []
  while True:
    print("Sai Dinner") #edit to show your name
    print("__________")
    print('N for a new order')
    print('C to change an order')
    print('X for close orders and print the check')
    print('P for to print the check')
    print('M for manager options')
    print('Q for quit')
    user_menu_choice = input('Your choice: '.upper())
    if user_menu_choice in 'Q':
      print("Exiting... Thank you for visiting!")
      break
    elif user_menu_choice in 'X':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
      print('Closing orders and printing the check:')
      functions.print_check(order)
      order = functions.reset_order() 
      break
    elif user_menu_choice in 'N':
      print('New order')
      make_order(user_menu_choice,order)  #calls a function for adding to the orders
    elif user_menu_choice in 'C':
      print('Modify your current order:')
      order = modify_order(user_menu_choice,order)  # Modify the existing order
    elif user_menu_choice in 'P':
      if order == []:
          print("No Items, Please order first")
      else:
        functions.print_check(order)
    elif user_menu_choice == 'M':
            functions.update_menu()
    else:
      print("Invalid input. Please try again.")
 
def make_order(menu_choice, order):
  print('Functionality for menu choice ', menu_choice)
  while True:
   user_selection = functions.get_item_number()
   if user_selection:
      item_code, quantity = user_selection
      item_name, item_price, stock = functions.get_item_information(item_code)
            if quantity <= stock:
                order.append((item_name, item_price, quantity))
                print(f"Added {quantity} of {item_name} to your order.")
            else:
                print(f"Sorry, we only have {stock} of {item_name}.")
      continue_order = input("Would you like to add more items? (Y/N): ").upper()
   if continue_order == 'N':
      break
  return order
 

def modify_order(menu_choice,order):
    print('Functionality for menu choice ', menu_choice)
    if not order:
        print("Your order is empty. Please add items first.")
        return order
    
    functions.display_current_order(order)
    while True:
        item_to_remove = int(input("Enter the item number you want to remove (0 to cancel): "))
        if item_to_remove == 0:
            break
        elif 1 <= item_to_remove <= len(order):
            removed_item = order.pop(item_to_remove - 1)
            print(f"Removed {removed_item[0]} from your order.")
        else:
            print("Invalid item number.")
        
        more_changes = input("Would you like to remove more items? (Y/N): ").upper()
        if more_changes == 'N':
         break
    return order

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    order = []
    #print(functions.get_item_information('D1'))
    show_main_menu()


