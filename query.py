from data import stock
from user import *
from tools import *


user_1 = add_user()
cart={}

while True:
    print("Insert the number for your next option")
    input_val = input("1. List items by warehouse\n2. Search an item and place an order\n3. Quit\n>")
    if input_val == "1":
        warehouse_1 = warehouse_selection()
        while True:
            print("List by:")
            list_option = int(input("1 - Product state\n2 - Category\n3 - Days in stock\n>"))
            if list_option > 0 and list_option < 4:
                sorted_warehouse = dict_sorter(warehouse_1, list_option)
                for item in sorted_warehouse:
                    print(item)
                break
            else:
                print("Unknown wish!")
       
    elif input_val == "2":
        search_item = input("Search for: ")
        total_count_in_warehouse = prod_counter("category", stock)
        count = total_count_in_warehouse[search_item.capitalize()]

        if count != 0:            
            print(f"Maximum availability: {count}")
            add_to = input("Add to cart? y/n\n>")
            if add_to.lower() == "y":
                quantity = int(input("Quantity: "))
                if count >= quantity:
                    cart[search_item] = str(quantity) 
                else:
                    print(f"There are not this many available. The maximum amount that can be ordered is {count}")                       
        else:
            print("Product not found")
            
    elif input_val == "3":
        break
    else:
        print("Unknown wish! Keep wishing!")

print("######################")     
print(f"You ordered {cart}")
print(f"Thank you for your visit {user_1.first_name}")
if len(cart) != 0:
    print("Your bill will be sent to:")
    print(f"Name: {user_1.first_name} {user_1.last_name}")
    print(f"Address: {user_1.delivery_address}")
    print("Order:")
    for key, value,  in cart.items():
        print(f"Item: {key}, ammount {value}") 



