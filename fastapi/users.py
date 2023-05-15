from fastapi import HTTPException, Depends 
from sqlalchemy.orm import Session 
import schemas
import models
from passlib.context import  CryptContext
import jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime
from database import get_db

pswd = CryptContext(schemes=['bcrypt'], deprecated =['auto'])


def generate_token(user):
    payload = {'user_id':user.id, 'exp':datetime.utcnow + timedelta(minutes=30)}
    token = jwt.encode(payload , 'secretKey' , algorithm='HS256')
    return {'acces_token':token}



def create_user( user : schemas.Users, db: Session):
  
    new_user = models.UserModel(
        username = user.username,
        password = pswd.hash(user.password)
    )
    username = db.query(models.UserModel).filter(models.UserModel.username == user.username).first()
    if username:
        raise HTTPException(status_code=401 , detail='User already exists')
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {new_user}



def login_user (user:schemas.Users, db : Session ):
    available_user = db.query(models.UserModel).filter(models.UserModel.username == user.username).first()
    if not available_user:
        raise HTTPException(status_code=404, detail='Cannot find user')
    if not pswd.verify(user.password , available_user.password ):
        raise HTTPException(status_code=404, detail='Invalid password')
    token= generate_token(available_user)
    return {
        'acces_token':token
    }




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except  Exception:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = db.query(models.UserModel).filter(models.UserModel.username == username ).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user
 
 
