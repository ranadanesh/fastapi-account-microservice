from passlib.context import CryptContext
import hashlib
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return hashlib.md5(bytes(password, 'utf-8')).hexdigest()

#
# def verify_password(password: str, hashed_password: str):
#     return pwd_context.verify(password, hashed_password)
