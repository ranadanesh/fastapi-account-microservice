from pydantic import BaseModel, EmailStr, constr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8)


class UserResponse(BaseModel):
    username: str


class UserLogin(BaseModel):
    username: str
    password: str

