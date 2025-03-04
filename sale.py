# This file contains functions to handle sales
# ENGM4620 Project

sale_history = []      # list to record sale history

# parent class for a sale
class Sale:
  def __init__(self, customer_name, items):
    self.customer_name = customer_name
    self.items = items

# child class that will update the stock after a sale  
class Update_Sale(Sale):
   def __init__(self, customer_name, items, stock):
     super().__init__(customer_name, items)
     self.stock = stock

   # check available stock
   def stock_check(self):
        for item_number, quantity in self.items.items():
            if item_number not in self.stock or self.stock[item_number]["stock"] < quantity:
                print(f"Not enough stock for {self.stock[item_number]['name']}.\n")
                return False
        return True

   # update stock after sale
   def update_stock(self):
      if self.stock_check():
         for item_number, quantity in self.items.items():
            self.stock[item_number]["stock"] -= quantity
         return True
      return False

# display sale details
   def display_sale(self):
      print(f"\nCustomer: {self.customer_name}\nThat's So Cute Clothes Purchase Details")
      print(f"{'Item #':<12} {'Name':<15} {'Quantity':<5}")
      for item_number, quantity in self.items.items():
         print(f"{item_number:<12} {self.stock[item_number]['name']:<15} {quantity:<5}")


# function to create a new sale
def new_sale(stock):
    customer_name = input("Enter customer name: ")
    num_items = {}

    while True:
      item_number = int(input("Enter item number (0 to finish): "))
      if item_number == 0:
         # create sale and complete stock update
         sale = Update_Sale(customer_name, num_items, stock)
         if sale.update_stock():
            sale.display_sale()
            sale_history.append({"customer_name": customer_name, "items": num_items})
         else:
            print("Not enough stock, sale unsuccessful!\n")
         break  # stop adding items
          
      if item_number not in stock:
         print("Invalid item number, please try again!")
         continue
          
      quantity = int(input(f"Enter quantity of {stock[item_number]['name']}: "))
      if quantity <= 0:
         print("Invalid quantity, please try again!")
         continue

      num_items[item_number] = quantity
      if not num_items:
         print("No items selected, sale unsuccessful!\n")
         return

# function to display sale history
def view_sale_history(stock):
   print("\nSale History")
   if not sale_history:
      print("No sales recorded.\n")
   else:
      for sale in sale_history:
         print(f"Customer: {sale['customer_name']}")
         print(f"{'Item #':<12} {'Name':<15} {'Quantity':<5}")
         for item_number, quantity in sale["items"].items():
            print(f"{item_number:<12} {stock[item_number]['name']:<15} {quantity:<5}")