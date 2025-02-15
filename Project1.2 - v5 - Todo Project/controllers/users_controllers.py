from routes.login_routes import LoginRoutes
from controllers.todo_controllers import TodoControl

import asyncio

class UserControl(TodoControl):
    def __init__(self):
        super().__init__()
        self.login_routes = LoginRoutes()
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
    
    def initialize_todo(self, user_id):
        print("Initialize Todo Playground!")
        
        while True:
            control = input("Type 'Create', 'Read', 'Update', 'Delete' or 'Logout': ").lower()
            if control == "create":
                self.create_todo(user_id)
                # return False
            elif control == "read":
                self.read_todo(user_id)
                # return False
            elif control == "update":
                self.update_todo(user_id)
                # return False
            elif control == "delete":
                self.delete_todo(user_id)
                # return False
            elif control == "logout":
                self.shutdown_app()
                return False
            else:
                print(f"Invalid! You type: {control} \n")
        
    def login(self):
        username = input(f"Enter username: ").lower()
        password = input(f"Enter password: ")
        
        user_id = self.login_routes.login_user(username, password)
        self.initialize_todo(user_id)
    
    def register(self):
        email = input("Enter email: ").lower()
        username = input("Enter username: ").lower()
        password = input("Enter password: ")

        self.login_routes.register_user(email, username, password)
 
    def logout(self):
        print(f"User has logged out!")
        self.initialize_app()
        
    def change_password(self):
        print("Changing password")
        
    def shutdown_app(self):
        print("Thank you for playing todo app! I'll see you soon")