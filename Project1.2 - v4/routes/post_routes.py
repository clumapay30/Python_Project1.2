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
            print(user)

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
                
    def check_user_posts(self, user_id):
        cursor = None
        
        try: 
            cursor = self.conn.cursor()
            cursor.execute("""
                           SELECT posts.id, posts.content, posts.created_at, users.id AS user_id, users.username, users.email, users.password
                           FROM posts
                           JOIN users ON posts.user_id = users.id
                           WHERE users.id = %s
                           ORDER BY posts.user_id DESC;
                           """, (user_id,))
            posts = cursor.fetchall()
            if posts:
                print(f"Posts by User {user_id}:")
                for post in posts:
                    print(f"Post ID: {post[0]}, \n Content: {post[1]} \n Username: {post[4]}")
            else:
                print(f"No posts found for user id {user_id}.")
            return posts
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if self.conn is not None:
                self.conn.close()
                
    def check_all_posts(self):
        
        cursor = None
        try:
            cursor = self.conn.cursor()
            
            cursor.execute("""
                           SELECT posts.id, posts.content, posts.created_at, users.id AS user_id, users.username, users.email, users.password
                           FROM posts
                           JOIN users ON posts.user_id = users.id
                           ORDER BY posts.user_id DESC;
                           """)
            posts = cursor.fetchall()
            
            print(posts)
            
            return posts
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if self.conn:
                self.conn.close()