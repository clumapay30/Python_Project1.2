from config.database import Database

class Schemas:
    
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        
    def check_user_table(self):
        conn = None
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(30) UNIQUE NOT NULL,
                        password VARCHAR(100) NOT NULL,
                        email VARCHAR(100) UNIQUE NOT NULL
                    )
                """
            )
            
            self.conn.commit()
            print("Table 'users' is ready!")
        except Exception as e:
            print(f"Error ensuring table: {e}")
        finally:
            if self.conn:
                self.conn.rollback()
            if conn:
                cursor.close()
                self.db.release_connection(conn)
                
    def check_post_table(self):
        conn = None
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS posts (
                        id SERIAL PRIMARY KEY,
                        user_id INT NOT NULL,
                        content TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT NOW(),
                        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                    )
                """
            )
            
            self.conn.commit()
            print("Table 'posts' is ready!")
        
        except Exception as e:
            print(f"Error ensuring posts: {e}")
        
        finally:
            if self.conn:
                self.conn.rollback()
            if conn:
                cursor.close()
                self.db.release_connection(conn)