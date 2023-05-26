from fastapi import APIRouter, Depends, Request , Response 
import users
from sqlalchemy.orm import Session
from database import get_db
import schemas

router = APIRouter(
    prefix='/users'
)

@router.post('/')
def signup( user : schemas.Users, db : Session = Depends(get_db)):
    return users.create_user(user, db) 

@router.post('/signin')
def signin(user : schemas.Users , db : Session = Depends(get_db)):
    return users.login_user(user, db )


@router.post('/signout')
def signout(request : Request , response : Response ):
    return users.signout_user(request ,response )


