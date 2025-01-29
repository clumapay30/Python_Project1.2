from routes.post_routes import PostRoutes

class PostController:
    
    def __init__(self):
        self.post_routes = PostRoutes()
        
    def create_post(self, id):
        user_id = int(id)
        content = input("Type your post: ")

        self.post_routes.create_post(user_id, content)

    def all_posts(self):
        self.post_routes.check_user_posts()
        
    def user_posts(self, id):
        self.post_routes.check_user_posts(id)