from psycopg2 import pool

class Database:
    
    def __init__(self):
        self.DB_CONFIG = {
            "dbname": "funnel_db",
            "user": "postgres",
            "password": "Simplepersonitsme",
            "host": "localhost",
            "port": 5432
        }
        
        self.connection_pool = pool.SimpleConnectionPool(1,10, **self.DB_CONFIG)

    def get_connection(self):
        try:
            return self.connection_pool.getconn()
        except Exception as e:
            print(f"Error getting connection: {e}")
            raise
        
    def release_connection(self, conn):
        try:
            self.connection_pool.putconn(conn)
        except Exception as e:
            print(f"Error releasing connection: {e}")
            raise
        
    def close_all_connection(self):
        self.connection_pool.closeall()