from config.database import Database
from middlewares.auth import Authentication
from models.userModel import UserModel

class UserLoginRoutes:
    def __init__(self):
        self.auth = Authentication()
        self.user_model = UserModel()
        
        self.db = Database()
        self.conn = self.db.get_connection()
                
    def register_routes(self, email, username, password):
        self.user_model.check_user_table()
        hashed_password = self.auth.hashed_password(password)
        
        try:
            cursor = self.conn.cursor()
            
            insert_query = "INSERT INTO logins(email, username, password) VALUES(%s, %s, %s)"
            user_data = (email, username, hashed_password)
            
            cursor.execute(insert_query, user_data)
            self.conn.commit()
            print(f"{username} has been registered!")
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()
    
    def login_routes(self, username, password):
        try:
            cursor = self.conn.cursor()
            query = "SELECT EXISTS (SELECT 1 FROM logins WHERE username=%s)"
            cursor.execute(query, (username,))
            
            if cursor.fetchone()[0]:
                user_query = "SELECT * FROM logins WHERE username=%s"
                cursor.execute(user_query, (username,))
                
                db_data = cursor.fetchone()

                if self.auth.verify_password(password, db_data[3]):
                    print("Logged in successful!")
                    print(f"Data: {db_data}")
                else:
                    print("Wrong Credentials!")
            else:
                print("Wrong Credentials!")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        finally: 
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()
            