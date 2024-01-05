from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(UserCreate):
    id: int


users_db = []
user_id_counter = 1

def create_user(user_create: UserCreate):
    global user_id_counter
    new_user = User(id=user_id_counter, **user_create.dict())
    users_db.append(new_user)
    user_id_counter += 1
    return new_user

def get_user_by_id(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    return None
