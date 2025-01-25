from config.db import Database
import psycopg2

class Middleware:
    
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
    
    def login_auth(self, username):
        try:
            cursor = self.conn.cursor()
            query = "SELECT password FROM users WHERE username = %s"
            user_data = (username,)

            cursor.execute(query, user_data)

            data_password = cursor.fetchone()
            
            # print(data_password[0])
            return data_password[0]
        
        except psycopg2.Error as e:
            print(f"An error occurred: {e}")

        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()