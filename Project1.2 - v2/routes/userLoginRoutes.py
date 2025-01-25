from config.db import Database
from middlewares.auth import Authentication

class UserLoginRoutes:
    def __init__(self):
        self.auth = Authentication()
        
        self.db = Database()
        self.conn = self.db.get_connection()
        
    def check_user_table(self): 
        # this function should be in models folder
        conn = None
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                           CREATE TABLE IF NOT EXISTS logins (
                               id SERIAL PRIMARY KEY,
                               email VARCHAR(100) UNIQUE NOT NULL,
                               username VARCHAR(100) UNIQUE NOT NULL,
                               password VARCHAR(100)
                           )
                           """
            )

            self.conn.commit()
            print("Table 'Logins' is ready!")
            
        except Exception as e:
            print(f"Error ensuring table: {e}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                cursor.close()
                # self.db.release_connection(conn)
                
    def register_routes(self, email, username, password):
        self.check_user_table()
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
            