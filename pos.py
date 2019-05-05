import os
from pos_user import *

clear = "cls"
current_app = "main"
current_user = None
all_users = []

all_users.append(User("admin", "1234", 3))

def login(u_input, p_input):
        found = False
        global current_user
        for u in all_users:
            if u_input == u.username and p_input == u.password:
                current_user = u
                return True
            else:
                print("\nLogin credentials are incorrect.")
                return False

def main_menu():
    input("\nPress enter for main menu.")
    os.system(clear)
    print("What would you like to do?\n")
    print("1 - Create a Sell")
    print("2 - Add Inventory")
    print("3 - Audit Transactions")
    print("4 - Manage Users")
    print("5 - Logout")
    return input("\nChoose an option, 1-5: ")

def inventory_mgmt():
    print("What would you like to do?\n")
    print("1 - Add Inventory")
    print("2 - Remove Inventory")
    print("3 - Main Menu")
    return input("\nChoose an option, 1-3: ")

def user_mgmt():
    print("What would you like to do?\n")
    print("1 - Create a User")
    print("2 - Remove a User")
    print("3 - Edit a User")
    print("4 - Main Menu")
    return input("\nChoose an option, 1-4: ")

while True:
    if current_user == None:
        os.system(clear)
        u_input = input("Username: ")
        p_input = input("Password: ")
        found = login(u_input, p_input)

    if current_app == "main":
        menu_option = int(main_menu())
        if menu_option == 1:
            pass
        elif menu_option == 2:
            if current_user.role in range(2,4):
                current_app = "inventory"
            else:
                print("\nYou do not have access to that.")
        elif menu_option == 3:
            pass
        elif menu_option == 4:
            current_app = "user"
        elif menu_option == 5:
            os.system(clear)
            break

    if current_app == "inventory":
        os.system(clear)
        inventory_mgmt_input = int(inventory_mgmt())
        if inventory_mgmt_input == 1:
            pass
        elif inventory_mgmt_input == 2:
            pass
        elif inventory_mgmt_input == 3:
            current_app = "main"

    if current_app == "user":
        os.system(clear)
        users_mgmt_input = int(user_mgmt())
        if users_mgmt_input == 1:
            pass
        elif users_mgmt_input == 2:
            pass
        elif users_mgmt_input == 3:
            pass
        elif users_mgmt_input == 4:
            current_app = "main"
