from sqlalchemy import Column , String , Integer 
from database import Base 



class UserModel(Base):
    __tablename__ = 'users/fastapi'
    id = Column(Integer , primary_key= True , index = True )
    username = Column(String , nullable = False )
    password = Column(String , nullable  = False )



class PostsModel(Base):
    __tablename__ = 'posts/fastapi'
    id = Column(Integer , primary_key=True , index = True)
    title = Column(String , nullable=False )
    content = Column(String , nullable = False)

    