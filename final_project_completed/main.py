# Final Project IT412
# Main Module 

from functions.functions import *

# Main Menu selection for user to choose
while (True):
    print("\nMenu: \n1. Import Data into the Database \n2. Show Data currently in Database \n3. Add Record to Databases \n4. Edit a Record \n5. Quit the Program")
    menu_choice = input("Enter your choice: ")

    if menu_choice == "1":
        import_data()

    if menu_choice == "2":
        display_data()

    if menu_choice == "3":
        add_record()

    if menu_choice == "4":
        edit_records()

    if menu_choice == "5":
        break            