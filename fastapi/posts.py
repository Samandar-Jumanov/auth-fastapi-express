import models 
import fastapi
import database
import sqlalchemy
from sqlalchemy.orm import Session 
router = fastapi.APIRouter(
    prefix='/posts'
)



@router.get('/allposts')
def all(db : Session = fastapi.Depends(database.get_db) , curr_user = fastapi.Depends(database.authanticate)):
    all_posts = db.query(models.PostsModel).all()
    return all_posts