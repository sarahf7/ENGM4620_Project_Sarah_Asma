# This file contains the main function that runs the program
# ENGM4620 Project

# import necessary modules
from employees import *
from customers import *

# function to display main menu
def main_menu():
  print("\nWelcome to That's So Cute Clothes")
  print("1. Employee")
  print("2. Customer")
  print("3. Exit")

# main function
def main():
  while True:
    main_menu()
    choice = input("Select an option: ")
    if choice == "1":
      id = input("\nEnter 4-digit employee ID: ")
      if int(id) >= 1000 and int(id) < 10000:
        employee_portal()
      else:
        print("Invalid ID. Please try again.")
    elif choice == "2":
        customer_portal()
    elif choice == "3":
      print("\nBye!")
      break
    else:
      print("Invalid choice, please try again.")

# run the program
if __name__ == "__main__":
  main()