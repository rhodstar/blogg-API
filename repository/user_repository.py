from sqlalchemy.orm import Session
from models.user import User
from utils.hashing import Hash

def create(request: User,db: Session):
  secure_password = Hash.bycript(request.password)
  new_user = User(name=request.name, email=request.email, password=secure_password)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def get(id: int, db: Session):
  return db.query(User).filter(User.id == id).first()

  