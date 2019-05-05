class Item():

    def __init__(self, inum, name, quantity=0, price=0):
        self.inum = inum
        self.name = name
        self.quantity = quantity
        self.price = round(price, 2)

    def add_quantity(self, amount):
        self.quantity += amount

    def remove_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        else:
            return False

    def set_price(self, price):
        self.price = price

def get_lengths(inventory):
    lengths = [0,0]
    for index, i in enumerate(inventory):
        if len(i.name) + 2 > lengths[0]:
            lengths[0] = len(i.name) + 2
        if len(str(i.quantity)) + 2 > lengths[1]:
            lengths[1] = len(str(i.quantity)) + 2
    return lengths

def list_inventory(inventory):
    lengths = get_lengths(inventory)
    print("\n")
    for i in inventory:
        print(f"{i.inum:<6}{i.name:<{lengths[0]}}{i.quantity:<{lengths[1]}}{'${:,.2f}'.format(i.price):>8}")
    print('\n')
    input("Press enter to return to the inventory menu.")

def add_inventory(inventory):
    inum = input("\nItem Number: ")
    if len(str(inum)) != 4:
        input("Item Number must be 4 digits. Press enter to return to inventory menu.")
    else:
        found = False
        item_index = 0
        for index, i in enumerate(inventory):
            if inum == i.inum:
                found = True
                item_index = index
        if found:
            quantity = int(input(f"\nHow many {inventory[item_index].name} would you like to add: "))
            #inventory[item_index].add_quantity(quantity)
            return [item_index, quantity]
        else:
            item_name = input("Item Name: ")
            item_quantity = input("Item Quantity: ")
            item_price = float(input("Item Price: "))
            return [inum, item_name, item_quantity, item_price]
