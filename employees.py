# This file contains functions for the employee portal
# ENGM4620 Project

# import necessary modules
from stock import *
from sale import *

# function for employees portal
def employee_portal():
  while True:
    employee_menu()
    employee_choice = input("Select an option: ")
    if employee_choice == "1":
      view_stock()
    elif employee_choice == "2":
      new_sale(stock)
    elif employee_choice == "3":
      view_sale_history(stock)
    elif employee_choice == "4":
      add_inventory()
    elif employee_choice == "5":
      break
    else:
      print("Invalid choice, please try again.")

# function to display employees menu
def employee_menu():
  print("\nEmployee Portal")
  print("1. View Stock")
  print("2. Create a Sale")
  print("3. View Sale History")
  print("4. Add Stock (New Inventory)")
  print("5. Back to Main Menu")