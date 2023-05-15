from sqlalchemy.orm import sessionmaker  
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import jwt 
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()
Base = declarative_base()
db = 'postgresql://postgres:EDB builds software for teams who need to do more and go faster with PostgreSQL.@localhost/auth'
engine = create_engine(db)


SessionLocal = sessionmaker(autoflush = False , autocommit = False ,bind = engine )


def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


def authanticate (credientals : HTTPAuthorizationCredentials = Depends(security)):
     try:
         bearer = credientals.scheme
         token = credientals.credentials
         if bearer !='bearer' or not token:
            raise HTTPException(status_code=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED, detail='Invalid creadeintals')
         return jwt.decode(token , 'secret')
     except  Exception:
         raise HTTPException(status_code=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED, detail='Invalid creadientals')

     
     
     