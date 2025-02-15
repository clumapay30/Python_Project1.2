from config.database import Database
from models.schemas import Schemas
from middlewares.auth import Authentication

class TodoRoutes:
    def __init__(self):
        self.schemas = Schemas()
        self.auth = Authentication()
        
    def create_todo(self, user_id, todo):
        self.schemas.check_todo_table()
        
        db = Database()
        conn = db.get_connection()
        
        try:
            cursor = conn.cursor()
            
            cursor.execute("SELECT id FROM users WHERE id = %s;", (user_id,))
            user = cursor.fetchone()
            print(user)

            if not user:
                raise ValueError(f"User with id {user_id} does not exists!")

            cursor.execute(
                """
                    INSERT INTO todo (user_id, todo, created_at)
                    values (%s, %s, NOW())
                    RETURNING id;
                """,
                (user_id, todo)
            )
            
            todo_id = cursor.fetchone()[0]
            
            conn.commit()
            
            print(f"Post created with ID: {todo_id}")
            return todo_id
        
        except Exception as e:
            print("Error: {e}")
            raise
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
                
    def check_user_todo(self, user_id):
        cursor = None

        db = Database()
        conn = db.get_connection()
        
        try: 
            cursor = conn.cursor()
            cursor.execute("""
                           SELECT todo.id, todo.todo, todo.created_at, users.id AS user_id, users.username, users.email, users.password
                           FROM todo
                           JOIN users ON todo.user_id = users.id
                           WHERE users.id = %s
                           ORDER BY todo.user_id DESC;
                           """, (user_id,))
            todos = cursor.fetchall()
            if todos:
                print(f"Todo by User {user_id}:")
                for todo in todos:
                    print(f"Todo ID: {todo[0]}, \n Content: {todo[1]} \n Username: {todo[4]}\n")
            else:
                print(f"No todo found for user id {user_id}.")
            # return todos
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    
    def update_todo(self, user_id, todo_id, todo_content):
        cursor = None
        
        db = Database()
        conn = db.get_connection()
        
        try: 
            cursor = conn.cursor()
            cursor.execute("""
                           UPDATE todo
                           SET todo = %s 
                           WHERE id = %s AND user_id = %s
                           """, (todo_content, todo_id, user_id)
                           )
            
            conn.commit()
            
            self.check_user_todo(user_id)
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
    
    
    def delete_todo(self, user_id, todo_id):
        cursor = None
        
        db = Database()
        conn = db.get_connection()
        
        try: 
            cursor = conn.cursor()
            cursor.execute("""
                           DELETE FROM todo 
                           WHERE id = %s AND user_id = %s
                           """, (todo_id, user_id)
                           )
            
            conn.commit()
            self.check_user_todo(user_id)
        
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
                
    def check_all_todo(self):
        
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