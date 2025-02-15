from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

import os

class Database:
    def __init__(self):
        load_dotenv()
        self.connection_pool = SimpleConnectionPool(
            minconn=int(os.getenv("DATABASE_MIN_CONN")),
            maxconn=int(os.getenv("DATABASE_MAX_CONN")),
            host=os.getenv("DATABASE_HOST"),
            database=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            port=int(os.getenv("DATABASE_PORT")),
        )
        
        def get_connection(self):
            try:
                return self.connection_pool.getconn()
            except Exception as e:
                print(f"Error connection: {e}")
                raise
            
        def release_connection(self, conn):
            try:
                self.connection_pool.putconn(conn)
            except Exception as e:
                print(f"Error releasing connectoin: {e}")
                raise
            
        def close_all_connection(self):
            if self.connection_pool:
                self.connection_pool.closeall()