import os
from pos_user import *
from pos_inventory import *

clear = "cls"
current_app = "main"
current_user = None
all_users = []
inventory = []

#Build test data
all_users.append(User("admin", "1234", 3))
inventory.append(Item("0001", "Skull Shirt", 5, 15.99))
inventory.append(Item("0002", "Bro Shirt", 3, 12.99))
inventory.append(Item("0003", "Tiger Board Short", 6, 19.99))
inventory.append(Item("0004", "Khaki Cargo Short", 8, 21.99))
inventory.append(Item("0005", "Skull Sticker", 25, 1.99))

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
    print("2 - Manage Inventory")
    print("3 - Audit Transactions")
    print("4 - Manage Users")
    print("5 - Logout")
    return input("\nChoose an option, 1-5: ")

def inventory_mgmt():
    print("What would you like to do?\n")
    print("1 - Add Inventory")
    print("2 - Remove Inventory")
    print("3 - List Inventory")
    print("4 - Main Menu")
    return input("\nChoose an option, 1-4: ")

def user_mgmt():
    print("What would you like to do?\n")
    print("1 - Create a User")
    print("2 - Remove a User")
    print("3 - Edit a User")
    print("4 - List Users")
    print("5 - Main Menu")
    return input("\nChoose an option, 1-5: ")

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
            list_inventory(inventory)
        elif inventory_mgmt_input == 4:
            current_app = "main"

    if current_app == "user":
        os.system(clear)
        users_mgmt_input = int(user_mgmt())
        if users_mgmt_input == 1:
            new_user = create_user(all_users)
            if new_user:
                all_users.append(User(new_user[0], new_user[1], new_user[2]))
        elif users_mgmt_input == 2:
            pass
        elif users_mgmt_input == 3:
            pass
        elif users_mgmt_input == 4:
            list_users(all_users)
        elif users_mgmt_input == 5:
            current_app = "main"
