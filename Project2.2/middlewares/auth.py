from passlib.context import CryptContext

class Authentication:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hashed_password(self, password):
        hashed_password = self.pwd_context.hash(password)
        return hashed_password

    def verify_password(self, plain_password: str, hashed_password: str):
        status = self.pwd_context.verify(plain_password, hashed_password)
        return status