from routes.todo_routes import TodoRoutes


import asyncio

class TodoControl:
    def __init__(self):
        self.todo_routes = TodoRoutes()
    
    def create_todo(self, user_id):
        user_id = int(user_id)
        print(user_id)
        todo = input("Enter todo: ")
        
        self.todo_routes.create_todo(user_id, todo)
    
    def read_todo(self, user_id):
        user_id = int(user_id)
        print(user_id)
        self.todo_routes.check_user_todo(user_id)
    
    def update_todo(self, user_id):
        user_id = int(user_id)
        todo_id = int(input("Please enter todo ID you want to Update: "))
        updated_todo = input("Please enter the updated todo: ")
        
        self.todo_routes.update_todo(user_id, todo_id, updated_todo)
              
    def delete_todo(self, user_id):
        user_id = int(user_id)
        # print(user_id)
        todo_id = int(input("Please enter todo ID you want to delete: "))
        
        self.todo_routes.delete_todo(user_id, todo_id)
        