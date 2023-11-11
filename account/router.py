import asyncio
import motor.motor_asyncio
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends
from pymongo import MongoClient
from .settings import port, mongodb_uri
from .schemas import UserCreate, UserLogin, UserResponse
from fastapi import status
# from .services import UserService, get_user_service
from .db import collection
from .utils import hash_password
router = APIRouter(tags=["home/"])


@router.post('/user/create', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    # await user_service.create_user(user)
    # return {"message": "User Registered Successfully..."}

    # create_data = collection.insert_one(user.dict())
    # return {'user_id': str(create_data)}

    check_user = await collection.find_one({'username': user.username})
    if check_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This Username Has Been Taken! Please Choose Another Username")

    user.password = hash_password(user.password)
    result = await collection.insert_one(user.model_dump())
    print(result)

    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User didn't create")
    return user.model_dump()



@router.post('/login', status_code=status.HTTP_200_OK)
async def login_user(user: UserLogin):

    find_user = await collection.find_one({"email": user.email, "password": hash_password(user.password)})

    if not find_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Credentials!')

    return {"message": "User Logged In Successfully..."}



    # user_info = await collection.find_one({"username": user.username})
    # print(user_info)
    # if user_info:
    #     if user_info['password'] == user.password:
    #         return "User Logged In Successfully..."
    #     else:
    #         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password is incorrect.")
    # else:
    #     print('your account does not exist, please create an account first')
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

# if __name__ == "__main__":
#     client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_uri)
#     loop = asyncio.get_event_loop()




