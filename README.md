# auth-fastapi-express

#Express :
jsonwebtoken 
bcrypt 
sequelize 
postgresql
pg 
Only problem is after i created user it is not saving user to the db correctly 

#FastApi
sqlalchemy 
pydantic
passlib
pyjwt 


#Code corrected to save db 
instead of sequelize.sync({force : true })  Dont use {force : true}
