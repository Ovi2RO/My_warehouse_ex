from data import warehouse1, warehouse2
from user import *
from tools_func import *
from wa import *


user_1 = add_user()
warehouse_1 = warehouse_selection()
cart={}

while True:
    print("Insert the number for your next option")
    input_val = input("1. List items by warehouse\n2. Search an item and place an order\n3. Quit\n>")
    if input_val == "1":
        print(f"Items in {warehouse_1.name}")
        for prod in warehouse_1.products:
            print(prod)
        
    elif input_val == "2":
        search_item = input("Search for: ")
        if search_item in warehouse_1.products:
            count = 0
            for item in warehouse_1.products:
                if item == search_item:
                    count += 1
            
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
        
print(f"You ordered {cart}")
print(f"Thank you for your visit {user_1.first_name}")
if len(cart) != 0:
    print("Your bill will be sent to:")
    print(f"Name: {user_1.first_name} {user_1.last_name}")
    print(f"Address: {user_1.delivery_address}")
    print("Order:")
    for key, value,  in cart.items():
        print(f"Item: {key}, ammount {value}") 



