from data import warehouse1, warehouse2

class Warehouse:
    def __init__(self, products:list, name:str):
        self.products = products
        self.name = name

def warehouse_selection():
    print("Please type in your selection:")
    selection = input("Warehouse1, Warehouse2, Both\n>")

    if selection.lower() == "warehouse1":
        warehouse = Warehouse(warehouse1, "Warehouse 1")
    elif selection.lower() == "warehouse2":
        warehouse = Warehouse(warehouse2, "Warehouse 1")
    else:
        warehouse = Warehouse(warehouse1 + warehouse2, "Both warehouses")
    return warehouse