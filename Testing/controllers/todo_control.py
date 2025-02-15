
class TodoControl:
    def __init__(self):
        self.initialize_todo()
    
    def initialize_todo(self):
        print("Initialize Todo Playground!")
        while True:
            control = input("Type 'Create', 'Read', 'Update', or 'Delete': ").lower()
            if control == "create":
                self.create_todo()
                return False
            elif control == "read":
                self.read_todo()
                return False
            elif control == "update":
                self.update_todo()
                return False
            elif control == "delete":
                self.delete_todo()
                return False
            else:
                print(f"Invalid! You type: {control} \n")
    
    def create_todo(self, id=1):
        user_id = int(id)
        todo = input("Enter todo: ")
    
    def read_todo(self, id=1):
        pass
    
    def update_todo(self, id=1):
        user_id = int(id)
        todo_id = int(input("Please enter todo ID you want to update: "))
        updated_todo = input("Please enter updated todo: ")
        
        
    def delete_todo(self, id=1):
        user_id = int(id)
        todo_id = int(input("Please enter todo ID you want to delete: "))
        delete_todo = int(input("Please enter the ID of the todo: "))
        