# This file contains functions to handle stock of items
# ENGM4620 Project

# original stock
stock = {1: {"name": "T-Shirt", "stock" : 10},
         2: {"name": "Pants", "stock" : 5},
         3: {"name": "Heels", "stock" : 10},
         4: {"name": "Purse", "stock" : 3}
        }

# function to display the stock
def view_stock():
    print("\nThat's So Cute Stock:")
    print(f"{'Item #':<12} {'Name':<15} {'Stock':<5}")
    for item_number, item in stock.items():
      print(f"{item_number:<12} {item['name']:<15} {item['stock']:<5}")

# function for employee to add stock 
def add_inventory():
    item_number = int(input("Please enter the item number: "))
    
    # add stock to existing item 
    if item_number in stock:
        add_stock = int(input(f"Enter additional stock for {stock[item_number]['name']}: "))
        stock[item_number]["stock"] += add_stock
        print(f"{add_stock} additional stock for {stock[item_number]['name']} has been added!\n")
    
    #add new item
    else:
        print("New item detected!")
        item_name = input(f"Enter name for item {item_number}: ")
        item_stock = int(input("Enter initial stock quantity: "))
        stock[item_number] = {"name": item_name, "stock": item_stock}        # add new item to stock dictionary
        print(f"New item {item_name} with {item_stock} has been added!")            #display message that inventory has been added 
        
    