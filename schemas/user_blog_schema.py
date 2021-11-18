from typing import List
from pydantic import BaseModel
from .blog_schema import Blog

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
  title: str
  body: str
  creator: ShowUser

  class Config():
    orm_mode = True