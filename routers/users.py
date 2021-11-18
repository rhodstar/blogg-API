from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from schemas.user_schema import ShowUser, User
from sqlalchemy.orm import Session
from repository import user_repository

router = APIRouter(
  prefix="/users",
  tags=['Users']
)

@router.post('/', response_model=ShowUser)
def create(request: User,db: Session = Depends(get_db)):
  return user_repository.create(request,db)

@router.get('/{id}', response_model=ShowUser)
def show(id: int, db: Session=Depends(get_db)):
  res = user_repository.get(id, db)
  if not res:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f"User with id {id} not found")
  return res