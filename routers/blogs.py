from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from schemas.user_blog_schema import ShowBlog, Blog
from schemas.user_schema import User
from sqlalchemy.orm import Session
from repository import blog_repository
from utils import oauth2

router = APIRouter(
  prefix="/blogs",
  tags=['Blogs']
)

@router.get('/', response_model=List[ShowBlog])
def all(db: Session = Depends(get_db),
  #Auth
  current_user: User=Depends(oauth2.get_current_user)):
  return blog_repository.get_all(db)

@router.get('/{id}', status_code=200, response_model=ShowBlog)
def show(id: int, db: Session=Depends(get_db),
  #Auth
  current_user: User=Depends(oauth2.get_current_user)):
  res = blog_repository.get(id, db)
  if not res:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Blog with id {id} not found")
  return res

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db),
  #Auth
  current_user: User=Depends(oauth2.get_current_user)):
  return blog_repository.save(request,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: Blog, db: Session=Depends(get_db),
  #Auth
  current_user: User=Depends(oauth2.get_current_user)):
  res = blog_repository.update(id, request, db)
  if not res:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
      detail=f"Blog with id {id} not found")
  
  return res

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(request: Blog, db: Session=Depends(get_db),
  #Auth
  current_user: User=Depends(oauth2.get_current_user)):
  res = blog_repository.delete(id,db)
  if not res:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Blog with id {id} not found")
    
  return {"message": "Blog succesfully deleted"}