from routes.post_routes import PostRoutes

class PostController:
    
    def __init__(self, id):
        self.post_routes = PostRoutes()
        self.create_post(id)
        
    def create_post(self, id):
        user_id = int(id)
        content = input("Type your post: ")

        self.post_routes.create_post(user_id, content)