from routes.user_routes import *
from middleware.error_middleware import *

class UserServer:
    def __init__(self):
        self.user_routes = User_Routes()
        self.middleware = Middleware()
        self.initialize()
                 
    def initialize(self):
        access = False
        
        while access == False:
            user_access = input("Do you want to login or signup: ").lower()
            
            if user_access == 'signup':
                self.signup()
                access = True
            elif user_access == 'login':
                self.login()
                access = True
            elif user_access == "delete":
                self.remove_user()
            else:
                print(f"Oops, you type '{user_access}' \nYou can only type 'Login', 'Signup' or 'Delete'! \n")
        
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        self.user_routes.read_user(username, password)
        # self.middleware.login_auth(username)
                
    def signup(self):
        firstname = input("Enter firstname: ")
        lastname = input("Enter lastname: ")
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
            
        self.user_routes.create_user(firstname, lastname, email, username, password)
    
    def remove_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        self.delete_user(username, password)