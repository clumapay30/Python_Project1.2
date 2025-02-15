from controllers.todo_control import TodoControl

class UserControl:
    def __init__(self):
        self.initialize_app()
    
    def initialize_app(self):
        while True:
            optin = input("Type 'Login' or 'Register': ").lower()
            
            if optin == "login":
                self.login()
                return False
            elif optin == "register":
                self.register()
                return False
            else:
                print(f"Invalid! You type: {optin} \n")
        
    def login(self):
        print("You have logged in!")
        todo = TodoControl()
    
    def register(self):
        print("Please register")
        
    def change_password(self):
        print("Changing password")