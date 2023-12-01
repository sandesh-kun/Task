import re

class User_acc:
    def __init__(self, u_name, passw, phone_number):
        # self.f_name = f_name
        # self.l_name = l_name
        self.u_name = u_name
        self.passw = passw
        self.phone_number = phone_number
        
    def password_strength(self, password):
        conditions = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
        
        if conditions.match(password):
            return f"Strong Password. Good to go."
        else:
            return f"Not valid password crieteria."
         
    def user_reg(self):
        
        self.u_name = input("Enter User Name: ")
        passw_input = input("Enter Password: ")
        check_password = input("Re-type password: ")
        
        if self.u_name:
             
            if passw_input == check_password:
                
                if self.password_strength(passw_input):
                    print("Account Created.")
                    self.passw = passw_input
                else:
                    print("Account not created.")
                    
            else:
                print("Both Password did not matched.")
                
        else:
            print("usernmae cannor be empty!")
            
    def user_login(self):
        name = input("Enter User Name: ")
        password = input("Enter Password: ")
        
        if name == self.u_name and password == self.passw:
            print("You are logged in...")
        else:
            print("Username or password does not match.")
            