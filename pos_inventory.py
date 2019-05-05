class Item():

    def __init__(self, inum, name, quantity=0, price=0, discount=0):
        self.inum = inum
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount

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
    lengths = [0,0,0]
    for index, i in enumerate(inventory):
        if len(i.name) + 2 > lengths[0]:
            lengths[0] = len(i.name) + 2
        if len(str(i.quantity)) + 2 > lengths[1]:
            lengths[1] = len(str(i.quantity)) + 2
        if len(str(i.price)) + 2 > lengths[2]:
            lengths[2] = len(str(i.price)) + 2
    return lengths

def list_inventory(inventory):
    lengths = get_lengths(inventory)
    print("\n")
    for i in inventory:
        print(f"{i.inum:<6}{i.name:<{lengths[0]}}{i.quantity:<{lengths[1]}}{round(i.price, 2):>{lengths[2]}}{i.discount:<}")
    print('\n')
    input("Press enter to return to the inventory menu.")
