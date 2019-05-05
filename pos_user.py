class User():
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def get_role(self):
        return self.role

def create_user(users):
    u_input = input("Username: ")
    found = False
    for u in users:
        if u.username == u_input:
            found = True
    if found:
        print("\nUsername is in use.")
        input("Press enter to return to main menu.")
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
