from routes.login_routes import LoginRoutes

from controllers.postController import PostController

class UserController:
    
    def __init__(self):
        self.login_routes = LoginRoutes()
        self.initialize_app()
    
    def initialize_app(self):
        print("Initializing Playground!")
        while True:
            optin = input("Type 'Login' or 'Register': ").lower()
            
            if optin == 'login':
                self.login()
                return False
            elif optin == 'register':
                self.register()
                return False
            else:
                print(f"Invalid: Your typed: {optin}! \n")
            
    def register(self):
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        self.login_routes.register_user(email, username, password)
    
    def login(self):
        username = input(f"Enter username: ")
        password = input(f"Enter password: ")

        id = self.login_routes.login_user(username, password)
        while True:
            create_post = input("Create a new post? Yes or No: ").lower()
            
            if create_post == 'yes':
                post = PostController()
                post.create_post(id)
                return False
            if create_post == "no":
                check_post = input("Do you want to check all users posts? Yes or No: ").lower()
                
                if check_post == "yes":
                    posts = PostController()
                    posts.user_posts(id)
                    return False
                else:
                    return False
            else: 
                print(f"Typo error: {create_post}")
    