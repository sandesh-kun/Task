import re

class User_acc:
    def __init__(self, u_name, passw, phone_number):
        self.u_name = u_name
        self.passw = passw
        self.phone_number = phone_number
        
    def password_strength(self, password):
        conditions = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        
        if conditions.match(password):
            return "Strong Password. Good to go."
        else:
            return "Not valid password criteria."
         
    def user_reg(self):
        # Prompt user for input
        self.u_name = input("Enter User Name: ")
        passw_input = input("Enter Password: ")
        check_password = input("Re-type password: ")
        
        if self.u_name:
            if passw_input == check_password:
                if self.password_strength(passw_input):
                    print("Account Created.")
                    self.passw = passw_input
                else:
                    print("Account not created. Password does not meet the required criteria.")
            else:
                print("Both Passwords did not match.")
        else:
            print("Username cannot be empty!")
            
    def user_login(self):
        # Prompt user for login credentials
        name = input("Enter User Name: ")
        password = input("Enter Password: ")
        
        if name == self.u_name and password == self.passw:
            print("You are logged in...")
        else:
            print("Username or password does not match.")

# Instantiate the User_acc class
user_account = User_acc("", "", "")

while True:
    # Display menu and get user command
    command = input("1. Registration \n2. Login \nEnter command: ")
    
    if command == '1':
        # Perform user registration
        user_account.user_reg()
        
    elif command == '2':
        # Perform user login
        user_account.user_login()
    else:
        # Handle invalid command
        print("Enter a valid command.")
