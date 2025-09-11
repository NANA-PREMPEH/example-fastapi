from pydantic import BaseModel, EmailStr, Field, conint
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel): # used for outputting user data
    id: int 
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut  # Include the owner information

    class Config:
        orm_mode = True

# class PostOut(PostBase):
#     post: Post
#     votes: int
    
    
#     class Config:
#         orm_mode = True
        
        
# Replace your PostOut class in app/schemas.py with this:
class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: UserOut
    votes: int
    
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None # -> fix here, from id to user_id, from str to int


class Vote(BaseModel):
    post_id: int
    dir: conint = Field(..., le=1)  # dir can only be 0 or 1