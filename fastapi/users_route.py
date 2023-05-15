from fastapi import APIRouter, Depends
import users
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models

router = APIRouter(
    prefix='/users'
)

@router.post('/')
def signup( user : schemas.Users, db : Session = Depends(get_db)):
    return users.create_user(user, db) 



