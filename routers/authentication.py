from fastapi import APIRouter, Depends, status, HTTPException
from fastapi. security import OAuth2PasswordRequestForm
from utils.hashing import Hash
from utils import token
from sqlalchemy.orm import Session
from database import get_db
from models.user import User

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
  user = db.query(User).filter(User.email == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Invalid credentials")

  if not Hash.verify(user.password, request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Invalid credentials.")
  
  access_token = token.create_access_token(data={"sub": user.email})
  return {"access_token": access_token, "token_type": "bearer"}