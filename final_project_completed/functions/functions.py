# Final Project IT412
# Functions Module

from classes.my_database_access import DB_Connect
from classes.entry import Entry
import json
import shutil
import os.path

def add_imported_record(entry):
    """Function used to gather all records from cleaned file and import to both databases"""
    my_db = DB_Connect('root', '', 'python_projects')

    f_name = entry.data["first_name"]
    l_name = entry.data["last_name"]
    address = entry.data["address"]
    city = entry.data["city"]
    state = entry.data["state"]
    zip = entry.data["zip"]
    company = entry.data["company_name"]
    primary_phone = entry.data["phone1"]
    secondary_phone = entry.data["phone2"]
    email_address = entry.data["email"]

    combined_name = (f_name + " " + l_name)

    my_db.executeQuery(f"INSERT into crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('{f_name}','{l_name}','{address}','{fixForSQL(city)}','{state}','{zip}','{fixForSQL(company)}','{primary_phone}','{secondary_phone}','{email_address}')")            
    my_db.executeQuery(f"INSERT into mailings (name, company, address) VALUES ('{combined_name}','{fixForSQL(company)}','{address}')")            
    my_db.conn.commit()

def add_record():
    """Function designed to gather all validation and inputs for record and submit to both databases"""
    my_db = DB_Connect('root', '', 'python_projects')

    f_name = get_valid_f_name()
    l_name = get_valid_l_name()
    address = get_valid_address()
    city = get_valid_city()
    state = get_valid_state()
    zip = get_valid_zip()
    company = get_valid_company()
    primary_phone = get_valid_prime_phone()
    secondary_phone = get_valid_second_phone()
    email_address = get_valid_email()

    combined_name = (f_name + " " + l_name)

    my_db.executeQuery(f"INSERT into crm_data (f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('{f_name}','{l_name}','{address}','{fixForSQL(city)}','{state}','{zip}','{fixForSQL(company)}','{primary_phone}','{secondary_phone}','{email_address}')")            
    my_db.executeQuery(f"INSERT into mailings (name, company, address) VALUES ('{combined_name}','{fixForSQL(company)}','{address}')")            
    print("\nNew customer record added to the databases!")
    my_db.conn.commit()

def display_crm_table():
    """Function used for displaying data in CRM table"""
    my_db = DB_Connect('root', '', 'python_projects')
    my_result = my_db.executeSelectQuery("SELECT * FROM crm_data")

    for record in my_result:
        print("__________________________________________", "\n")
        print("Customer ID#:", record["crm_id"])
        print("First Name:", record["f_name"])
        print("Last Name:", record["l_name"])
        print("Address:", record["address"])
        print("City:", record["city"])
        print("State:", record["state"])
        print("ZIP:", record["zip"])
        print("Company:", record["company"])
        print("Primary Phone:", record["primary_phone"])
        print("Secondary Phone:", record["secondary_phone"])
        print("Email:", record["email_address"])
    return display_data()

def display_data():
    """Function used for allowing user to choose which database data to display"""
    print("\nWhat database would you like to display: \n1. CRM Database \n2. Mailings Database \n3. EXIT to main menu")
        
    menu_choice = input("Enter your choice: ")

    if menu_choice == "1":
        display_crm_table()

    if menu_choice == "2":
        display_mailings_table()

    if menu_choice == "3":
        return

def display_mailings_table():
    """Function used for displaying data in mailing table"""
    my_db = DB_Connect('root', '', 'python_projects')
    my_result = my_db.executeSelectQuery("SELECT * FROM mailings")

    for record in my_result:
        print("__________________________________________", "\n")
        print("Mail ID#:", record["mail_id"])
        print("Name:", record["name"])
        print("Company:", record["company"])
        print("Address:", record["address"])
    return display_data()

def edit_crm_record():
    """Function used to edit the CRM records"""
    my_db = DB_Connect('root', '', 'python_projects')
    id = input("\nEnter the CRM ID: ")

    while (True):
        print("\nWhat field would you like to update: \n1. First Name \n2. Last Name \n3. Address \n4. City \n5. State \n6. ZIP Code \n7. Company \n8. Primary Phone \n9. Secondary Phone \n10. Email Address \n11. EXIT to Database Menu")
        menu_choice = input("\nEnter your choice: ")

        if menu_choice == "1":
            f_name = get_valid_f_name()
            my_db.executeQuery("UPDATE crm_data SET f_name = '" + f_name + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "2":
            l_name = get_valid_l_name()
            my_db.executeQuery("UPDATE crm_data SET l_name = '" + l_name + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "3":
            address = get_valid_address()
            my_db.executeQuery("UPDATE crm_data SET address = '" + address + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "4":
            city = get_valid_city()
            my_db.executeQuery("UPDATE crm_data SET city = '" + fixForSQL(city) + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "5":
            state = get_valid_state()
            my_db.executeQuery("UPDATE crm_data SET state = '" + state + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "6":
            zip = get_valid_zip()
            my_db.executeQuery("UPDATE crm_data SET zip = '" + zip + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "7":
            company = get_valid_company()
            my_db.executeQuery("UPDATE crm_data SET company = '" + fixForSQL(company) + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "8":
            primary_phone = get_valid_prime_phone()
            my_db.executeQuery("UPDATE crm_data SET primary_phone = '" + primary_phone + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "9":
            secondary_phone = get_valid_second_phone()
            my_db.executeQuery("UPDATE crm_data SET secondary_phone = '" + secondary_phone + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "10":
            email_address = get_valid_email()
            my_db.executeQuery("UPDATE crm_data SET email_address = '" + email_address + "' WHERE crm_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "11":
            return edit_records()

def edit_mailings_record():
    """Function used to edit the mailings records"""
    my_db = DB_Connect('root', '', 'python_projects')
    id = input("\nEnter the CRM ID: ")
    
    while (True):
        print("\nWhat field would you like to update: \n1. Name \n2. Company \n3. Address \n4. EXIT to Database Menu")
        menu_choice = input("\nEnter your choice: ")

        if menu_choice == "1":
            f_name = get_valid_f_name()
            l_name = get_valid_l_name()
            combined_name = (f_name + " " + l_name)
            my_db.executeQuery("UPDATE mailings SET name = '" + combined_name + "' WHERE mail_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "2":
            company = get_valid_company()
            my_db.executeQuery("UPDATE mailings SET company = '" + fixForSQL(company) + "' WHERE mail_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "3":
            address = get_valid_address()
            my_db.executeQuery("UPDATE mailings SET address = '" + address + "' WHERE mail_id = '" + id + "'")
            my_db.conn.commit()

        if menu_choice == "4":
            return edit_records()

def edit_records():
    """Function used for allowing user to choose which records to edit or remove in databases"""
    print("\nWhat database would you like to edit: \n1. CRM Database \n2. Mailings Database \n3. Remove Record \n4. EXIT to Main Menu")
    menu_choice = input("\nEnter your choice: ")

    if menu_choice == "1":
        edit_crm_record()

    if menu_choice == "2":
        edit_mailings_record()

    if menu_choice == "3":
        remove_record()

    if menu_choice == "4":
        return

def fixForSQL(self):
    """Function used to fix quotes for SQL queries"""
    fixedVersion = ''

    for char in self:
        fixedVersion += char
        if char == '\'':
             fixedVersion += '\''
    return fixedVersion

def get_valid_address():
    """Function used to get user address input"""

    while True:
        address = input("\nEnter the customer's street address: ")
        valid = is_valid_address(address)
        if valid:
            print("\nCustomer's street address updated!")
            return address
        else:
            print("\nInvalid address entered, please try again.")

def get_valid_city(): 
    """Function used to get user city input"""
    
    while True:
        city = input("\nEnter the customer's city: ")
        valid = is_valid_city(city)
        if valid:
            print("\nCustomer's city updated!")
            return city
        else:
            print("\nInvalid city entered, please try again.")

def get_valid_company(): 
    """Function used to get user company input"""
    company = input("\nEnter the customer's company (Optional): ")
    print('\nCompany name updated!')
    return company

def get_valid_email(): 
    """Function used to get user email input"""

    while True:
        email = input("\nEnter the customer's email address (Optional): ")
        valid = is_valid_email(email)
        if valid:
            print("\nCustomer's email address updated!")
            return email
        else:
            print("\nInvalid email entered, please try again.")

def get_valid_f_name(): 
    """Function used to get user's first name input"""

    while True:
        f_name = input("\nEnter the customer's first name: ")
        valid = is_valid_name(f_name)
        if valid:
            print("\nCustomer's first name updated!")
            return f_name
        else:
            print("\nInvalid first name entered, please try again.")

def get_valid_l_name(): 
    """Function used to get user's last name input"""

    while True:
        l_name = input("\nEnter the customer's last name: ")
        valid = is_valid_name(l_name)
        if valid:
            print("\nCustomer's last name updated!")
            return l_name
        else:
            print("\nInvalid last name entered, please try again.")

def get_valid_prime_phone(): 
    """Function used to get user primary phone input"""

    while True:
        primary_phone = input("\nEnter the customer's primary phone number: ")
        valid = is_valid_phone(primary_phone)
        if valid and not len(primary_phone) == 0:
            print("Customer's primary phone updated!")
            return primary_phone
        else:
            print("\nInvalid primary phone entered, please try again.")

def get_valid_second_phone():
    """Function used to get user secondary phone input"""

    while True:
        secondary_phone = input("\nEnter the customer's secondary phone number (Optional): ")
        valid = is_valid_phone(secondary_phone)
        if valid:
            print("\nCustomer's secondary phone updated!")
            return secondary_phone
        else:
            print("\nInvalid secondary phone entered, please try again.")

def get_valid_state():
    """Function used to get user state input"""

    while True:
        state = input("\nEnter the customer's state: (Uppercase Abbreviation) ")
        valid = is_valid_state(state)
        if valid:
            print("\nCustomer's state updated!")
            return state
        else:  
            print("\nInvalid state entered, please try again.")

def get_valid_zip():
    """Function used to get user ZIP code input"""

    while True:
        zip_code = input("\nEnter the customer's ZIP: ")
        valid = is_valid_zip(zip_code)
        if valid:
            print("\nCustomer's ZIP updated!")
            return zip_code
        else:
            print("\nInvalid ZIP entered, please try again.")

def import_data():
    """Function used to clean up text file, convert to other formats, backup if need be and call import function"""
    my_db = DB_Connect('root', '', 'python_projects')

    file = open("text_files\customer_export.txt", "r")
    lines = file.readlines()
    clean_data = []
    for line in lines:
        clean_data.append(line.strip().split("|"))

    all_entries = []
    for index in range(1, len(clean_data)):
        all_entries.append(Entry(clean_data[0], clean_data[index]))

    # Backup the CSV and JSON file 
    if os.path.isfile("text_files\customer_export.csv"):
        shutil.copy2("text_files\customer_export.csv", "text_files\customer_export.csv.backup")
    
    if os.path.isfile("text_files\customer_export.json"):
        shutil.copy2("text_files\customer_export.json", "text_files\customer_export.json.backup")

    # Writing to CSV file
    file = open("text_files\customer_export.csv", "w")
    file.write(all_entries[0].get_headerascsv() + "\n")
    for entry in all_entries:
        file.write(entry.getascsv() + "\n")
    file.close()

    # Writing to JSON file 
    file = open("text_files\customer_export.json", "w")
    file.write("[")
    for index in range(len(all_entries) -1):
        file.write(json.dumps(all_entries[index].data, indent=4) + ",\n")
    file.write(json.dumps(all_entries[-1].data, indent=4))
    file.write("]")
    file.close()
    
    # Purging the current data in databases 
    my_db.executeQuery("DELETE FROM crm_data")
    my_db.executeQuery("DELETE FROM mailings")
    my_db.conn.commit()
    
    # Writing to database
    for entry in all_entries:
        add_imported_record(entry)
    print("\nSuccesfully imported file into databases!")

def is_valid_address(address):
    """Function used to validate user address input"""
    invalid_chars = "!\"'@$%^&*_=+<>?;[]}{" 

    if len(address) == 0:
        return False
    for char in address: 
        if not (char.isalnum() or char.isspace() or char not in invalid_chars):
            return False
    return True

def is_valid_city(city):
    """Function used to validate user city input"""
    valid_chars = "'"

    if len(city) == 0:
        return False
    for char in city:
        if not (char.isalpha() or char.isspace() or char in valid_chars):
            return False
    return True

def is_valid_email(email):
    """Function used to validate user email input"""
    valid_chars = "@."

    for char in email:
        if not (char.isalnum() or char.isspace() or char in valid_chars):
            return False
    return True

def is_valid_name(name):
        """Function used to validate user names input"""
        valid_chars = "-'"

        for char in name:
            if not (char.isalpha() or char.isspace() or char in valid_chars):
                return False  
        return True

def is_valid_phone(phone):
    """Function used to validate user primary phone input"""
    valid_chars = "-"

    for char in phone:
        if not (char.isdigit() or char in valid_chars):
            return False
    return True

def is_valid_state(state):
    """Function used to validate user state input"""
    if state.isupper() and state.isalpha() and len(state) == 2:
        return True
    else:
        return False

def is_valid_zip(zip_code):
    """Function used to validate user ZIP code input"""

    if len(zip_code) != 4 and len(zip_code) != 5:
        return False
    for char in zip_code:
        if not char.isdigit():
            return False
    return True

def remove_crm_record():
    """Function used for deleting customer record from CRM database"""
    my_db = DB_Connect('root', '', 'python_projects')
    id = (input("\nEnter the CRM ID# of the record to be removed: "))
    choice = input("\nAre you sure you want to remove CRM record (y/n)?")

    if choice.lower() == 'y':
        my_db.executeQuery("DELETE FROM crm_data WHERE crm_id ='" + id + "'")
        my_db.conn.commit()
        print("\nRecord removed!")
    else:
        print("\nRecord not removed!")
        return remove_record()
  
def remove_mailings_record():
    """Function used for deleting mailing record from mailing database"""
    my_db = DB_Connect('root', '', 'python_projects')
    id = (input("\nEnter the mail ID# of the record to be removed: "))

    choice = input("\nAre you sure you want to remove mail record (y/n)?")
    if choice.lower() == 'y':
        my_db.executeQuery("DELETE FROM mailings WHERE mail_id ='" + id + "'")
        my_db.conn.commit()
        print('\nRecord removed!')
    else:
        print('\nRecord not removed!')
        return remove_record()

def remove_record():
    """Function used for providing a choice of which record to remove from which database"""
    print("\nWhat database would you like to remove record from: \n1. CRM Database \n2. Mailings Database \n3. EXIT to Database Menu")
        
    menu_choice = input("\nEnter your choice: ")

    if menu_choice == "1":
        remove_crm_record()
    
    if menu_choice == "2":
        remove_mailings_record()
    
    if menu_choice == "3":
        return edit_records()