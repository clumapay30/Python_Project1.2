from config.database import Database


class UserModel:
    
    def __init__(self):
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
            if self.conn:
                self.conn.rollback()
        finally:
            if conn:
                cursor.close()
                self.db.release_connection(conn)