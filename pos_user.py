class User():
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def get_role(self):
        return self.role

def get_lengths(users):
    lengths = [0,0]
    for index, u in enumerate(users):
        if len(u.username) + 2 > lengths[0]:
            lengths[0] = len(u.username) + 2
        if len(u.password) + 2 > lengths[1]:
            lengths[1] = len(u.password) + 2
    return lengths

def create_user(users):
    u_input = input("\nUsername: ")
    found = False
    for u in users:
        if u.username == u_input:
            found = True
    if found:
        print("\nUsername is in use.")
        input("\nPress enter to return to user menu.")
    else:
        p_input = input("Password: ")
        while True:
            print("\n1 - Sells User")
            print("2 - Inventory User")
            print("3 - Admin User")
            r_input = int(input("\nChoose role: (1-3) "))
            if r_input in range(1,4):
                return [u_input, p_input, r_input]
            else:
                continue

def list_users(users):
    lengths = get_lengths(users)
    print("\n")
    for u in users:
        print(f"{u.username:<{lengths[0]}}{u.password:<{lengths[1]}}{u.role:<}")
    print('\n')
    input("Press enter to return to the user menu.")
