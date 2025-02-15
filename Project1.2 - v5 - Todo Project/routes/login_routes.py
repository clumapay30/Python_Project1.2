from config.database import Database
from models.schemas import Schemas
from middlewares.auth import Authentication

class LoginRoutes:
    def __init__(self):
        self.schemas = Schemas()
        self.auth = Authentication()
    
    def register_user(self, email, username, password):
        self.schemas.check_user_table()
        
        db = Database()
        conn = db.get_connection()
        
        hashed_password = self.auth.hash_password(password)
        
        try:
            cursor = conn.cursor()
            
            insert_query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            user_data = (username, hashed_password, email)
            
            cursor.execute(insert_query, user_data)
            conn.commit()
            print(f"{username} has been registered!")
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
                
    def login_user(self, username, password):
        db = Database()
        conn = db.get_connection()
        
        try:
            cursor = conn.cursor()
            query = "SELECT EXISTS (SELECT 1 FROM users WHERE username=%s)"
            cursor.execute(query, (username,))

            if cursor.fetchone()[0]:
                user_query = "SELECT * FROM users WHERE username=%s"
                cursor.execute(user_query, (username,))

                db_data = cursor.fetchone()
                
                if self.auth.verify_password(password, db_data[2]):
                    print("Logged in successful!")
                    print(f"Data: {db_data} \n")
                    return db_data[0]
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
            if conn:
                conn.close()