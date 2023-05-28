from data import *
from datetime import datetime

def warehouse_selector(data_file:list, wanted_warehouse:int):
    warehouse_result = []
    for s_dict in data_file:
        if s_dict["warehouse"] == wanted_warehouse:
            warehouse_result.append(s_dict)
    return warehouse_result
#print(warehouse_selector(stock, 2))

def warehouse_selection():
    print("Please type in your selection:")

    while True:
        selection = int(input("1 for Warehouse1\n2 for Warehouse2\n3 for Both\n>"))
        if selection == 1:
            warehouse = warehouse_selector(stock, 1)
            break
        elif selection == 2:
            warehouse = warehouse_selector(stock, 2)
            break
        elif selection == 3:
            warehouse = stock
            break
        else:
            print("Unknown option, please try again!")
    return warehouse

########################################################################

def dict_sorter(warehouse_sort:list, sort_by:int):
    for item in warehouse_sort:
        item_date_obj = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
        item["days_in_stock"] = (datetime.today() - item_date_obj).days
    
    if sort_by == 1:
        result = sorted(warehouse_sort, key=lambda d: d["state"])
    elif sort_by == 2:
        result = sorted(warehouse_sort, key=lambda d: d["category"])
    elif sort_by == 3:
        result = sorted(warehouse_sort, key=lambda d: d["days_in_stock"])
    return result
#print(dict_sorter(stock, 3))







def prod_counter(prod:str, list_of_dict:list):
    result = {}
    for k in list_of_dict:
        if prod in k:
            result[k[prod]] = result.get(k[prod], 0) +1
    return result
print(prod_counter("category", stock))











