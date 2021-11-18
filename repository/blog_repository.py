from sqlalchemy.orm import Session
from models.blog import Blog

def get_all(db: Session):
  return db.query(Blog).all()

def get(int: id, db: Session):
  return db.query(Blog).filter(Blog.id == id).first()

def save(request: Blog, db: Session):
  new_blog = Blog(title=request.title,body=request.body, user_id=1)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

def update(id: int,request: Blog, db: Session):
  blog = db.query(Blog).filter(Blog.id == id)

  if not blog.first():
    return None
  
  blog.update(request)
  db.commit()
  return blog

def delete(id: int, db: Session):
  blog = db.query(Blog).filter(Blog.id == id)

  if not blog.first():
    return False
  
  blog.delete(synchronize_session=False)
  db.commit()
  return True