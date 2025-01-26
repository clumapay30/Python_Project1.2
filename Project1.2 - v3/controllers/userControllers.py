from routes.userLoginRoutes import UserLoginRoutes

class UserController(UserLoginRoutes):
    
    def __init__(self):
        
        super().__init__()
        # self.login_routes = UserLoginRoutes()
        self.initialize_app()
    
    def initialize_app(self):  
        print("Initialize Playground!")      
        while True:
            logic = input("Type 'Login', 'Register' or 'Forgot Password': ").lower()
            
            if logic == 'login':
                # print('You have Logged in!')
                self.login()
                return False
            elif logic == 'register':
                # print('Register new user')
                self.register()
                return False
            elif logic == 'forgot password':
                print('Forgot password initializing')
                return False
            else:
                print(f"Invalid: You typed '{logic}'! \n")
                
    def register(self):
        email = input(f"Enter valid email: ")
        username = input(f"Enter username: ")
        password = input(f"Enter password: ")

        self.register_routes(email, username, password)
        
    def login(self):
        username = input(f"Enter username: ")
        password = input(f"Enter password: ")

        self.login_routes(username, password) 