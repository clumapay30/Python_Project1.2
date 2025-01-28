from passlib.context import CryptContext

class Authentication:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
    def hash_password(self, password):
        hash_password = self.pwd_context.hash(password)
        return hash_password
    
    def verify_password(self, password, hashed_password):
        status = self.pwd_context.verify(password, hashed_password)
        return status