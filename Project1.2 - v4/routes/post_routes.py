from config.database import Database
from models.schemas import Schemas
from middlewares.auth import Authentication

class PostRoutes:
    def __init__(self):
        self.schemas = Schemas()
        self.auth = Authentication()
        
        self.db = Database()
        self.conn = self.db.get_connection()
        
    def create_post(self, user_id, content):
        self.schemas.check_post_table()
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("SELECT id FROM users WHERE id = %s;", (user_id,))
            user = cursor.fetchone()

            if not user:
                raise ValueError(f"User with id {user_id} does not exists!")

            cursor.execute(
                """
                    INSERT INTO posts (user_id, content, created_at)
                    values (%s, %s, NOW())
                    RETURNING id;
                """,
                (user_id, content)
            )
            
            post_id = cursor.fetchone()[0]
            
            self.conn.commit()
            
            print(f"Post created with ID: {post_id}")
            return post_id
        
        except Exception as e:
            print("Error: {e}")
            raise
            if self.conn:
                self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()