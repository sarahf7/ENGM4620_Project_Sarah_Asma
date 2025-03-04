# This file contains functions for the customer portal
# ENGM4620 Project

# import necessary modules
from stock import *

# function for customers portal
def customer_portal():
  while True:
    customer_menu()
    customer_choice = input("Select an option: ")
    if customer_choice == "1":
      view_stock()
    elif customer_choice == "2":
      break

# function to display the customers menu
def customer_menu():
  print("\nCustomer Portal")
  print("1. View Stock")
  print("2. Back to Main Menu")